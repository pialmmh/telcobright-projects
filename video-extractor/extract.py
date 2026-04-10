#!/usr/bin/env python3
"""
Software Feature Extractor
===========================
Extract knowledge graphs from YouTube software demo videos.

Usage:
    python extract.py "https://www.youtube.com/watch?v=VIDEO_ID" --name "Odoo CRM"
    
Requirements:
    pip install yt-dlp openai-whisper anthropic Pillow
    
    Also needs ffmpeg:
    - Mac: brew install ffmpeg
    - Ubuntu: sudo apt install ffmpeg
    - Windows: Download from ffmpeg.org
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
import base64

# Check dependencies
def check_dependencies():
    """Check if required tools are installed"""
    missing = []
    
    # Check ffmpeg
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append("ffmpeg")
    
    # Check yt-dlp
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append("yt-dlp (pip install yt-dlp)")
    
    # Check Python packages
    try:
        import whisper
    except ImportError:
        missing.append("openai-whisper (pip install openai-whisper)")
    
    try:
        import anthropic
    except ImportError:
        missing.append("anthropic (pip install anthropic)")
    
    if missing:
        print("❌ Missing dependencies:")
        for dep in missing:
            print(f"   - {dep}")
        print("\nInstall them and try again.")
        sys.exit(1)
    
    print("✅ All dependencies found")


def download_video(url: str, output_dir: Path) -> Path:
    """Download video from YouTube"""
    print(f"\n📥 Downloading video...")
    
    video_path = output_dir / "video.mp4"
    
    cmd = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]/best",
        "--merge-output-format", "mp4",
        "-o", str(video_path),
        url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Download failed: {result.stderr}")
        sys.exit(1)
    
    print(f"✅ Video saved to {video_path}")
    return video_path


def extract_frames(video_path: Path, output_dir: Path, interval: int = 5) -> list:
    """Extract frames every N seconds"""
    print(f"\n🎞️ Extracting frames every {interval} seconds...")
    
    frames_dir = output_dir / "frames"
    frames_dir.mkdir(exist_ok=True)
    
    cmd = [
        "ffmpeg", "-i", str(video_path),
        "-vf", f"fps=1/{interval}",
        "-q:v", "2",  # High quality
        str(frames_dir / "frame_%04d.jpg"),
        "-y"  # Overwrite
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    frames = sorted(frames_dir.glob("frame_*.jpg"))
    print(f"✅ Extracted {len(frames)} frames")
    
    # Create timestamp mapping
    frame_data = []
    for i, frame in enumerate(frames):
        frame_data.append({
            "index": i,
            "timestamp": i * interval,
            "path": str(frame),
            "filename": frame.name
        })
    
    return frame_data


def extract_audio(video_path: Path, output_dir: Path) -> Path:
    """Extract audio for transcription"""
    print(f"\n🔊 Extracting audio...")
    
    audio_path = output_dir / "audio.wav"
    
    cmd = [
        "ffmpeg", "-i", str(video_path),
        "-vn",  # No video
        "-acodec", "pcm_s16le",
        "-ar", "16000",  # 16kHz for Whisper
        "-ac", "1",  # Mono
        str(audio_path),
        "-y"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(f"✅ Audio saved to {audio_path}")
    return audio_path


def transcribe_audio(audio_path: Path, output_dir: Path, model_size: str = "base") -> dict:
    """Transcribe audio using Whisper"""
    print(f"\n🎤 Transcribing audio (using Whisper {model_size} model)...")
    print("   This may take a few minutes...")
    
    import whisper
    
    model = whisper.load_model(model_size)
    result = model.transcribe(
        str(audio_path),
        word_timestamps=True,
        language="en"
    )
    
    # Structure the output
    transcript = {
        "full_text": result["text"],
        "language": result.get("language", "en"),
        "segments": []
    }
    
    for seg in result["segments"]:
        transcript["segments"].append({
            "id": seg["id"],
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })
    
    # Save transcript
    transcript_path = output_dir / "transcript.json"
    with open(transcript_path, "w") as f:
        json.dump(transcript, f, indent=2)
    
    print(f"✅ Transcription complete ({len(transcript['segments'])} segments)")
    return transcript


def create_timeline(frames: list, transcript: dict, output_dir: Path) -> list:
    """Align frames with transcript segments"""
    print(f"\n⏱️ Creating synchronized timeline...")
    
    timeline = []
    
    for frame in frames:
        ts = frame["timestamp"]
        
        # Find matching transcript segment
        matching_text = ""
        for seg in transcript["segments"]:
            if seg["start"] <= ts < seg["end"]:
                matching_text = seg["text"]
                break
            elif seg["start"] <= ts + 2.5 and seg["end"] >= ts - 2.5:
                # Within 2.5 seconds
                matching_text = seg["text"]
        
        timeline.append({
            "timestamp": ts,
            "timestamp_formatted": f"{int(ts//60):02d}:{int(ts%60):02d}",
            "frame_path": frame["path"],
            "frame_filename": frame["filename"],
            "transcript": matching_text
        })
    
    # Save timeline
    timeline_path = output_dir / "timeline.json"
    with open(timeline_path, "w") as f:
        json.dump(timeline, f, indent=2)
    
    print(f"✅ Timeline created with {len(timeline)} entries")
    return timeline


def encode_image(image_path: str) -> str:
    """Encode image to base64"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def analyze_with_claude(timeline: list, software_name: str, output_dir: Path) -> dict:
    """Analyze screenshots and transcript with Claude"""
    print(f"\n🤖 Analyzing with Claude AI...")
    
    import anthropic
    
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY not set!")
        print("   Export your API key: export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)
    
    client = anthropic.Anthropic()
    
    # Process in batches of 5 frames
    batch_size = 5
    all_analyses = []
    
    for i in range(0, len(timeline), batch_size):
        batch = timeline[i:i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(timeline) + batch_size - 1) // batch_size
        
        print(f"   Processing batch {batch_num}/{total_batches}...")
        
        # Build message content with images
        content = []
        for entry in batch:
            content.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": encode_image(entry["frame_path"])
                }
            })
            content.append({
                "type": "text",
                "text": f"[{entry['timestamp_formatted']}] Audio: \"{entry['transcript']}\""
            })
        
        # Analysis prompt
        content.append({
            "type": "text",
            "text": f"""Analyze these sequential screenshots from a "{software_name}" software demonstration.

For EACH screenshot, provide a JSON object with:

1. "screen_name": Name of the current screen/page
2. "module": Which module (Sales, Inventory, CRM, etc.)
3. "feature_demonstrated": What feature is being shown
4. "user_action": What action the user is performing
5. "ui_components": List of visible UI elements with:
   - "type": button/form/table/modal/menu/etc
   - "label": Text label
   - "purpose": What it does
6. "data_shown": Any visible data fields, table columns, form fields
7. "navigation_context": Where this fits in the user journey
8. "business_process": What business process this supports

Return ONLY a JSON array with one object per screenshot, no other text."""
        })
        
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                messages=[{"role": "user", "content": content}]
            )
            
            # Parse response
            response_text = response.content[0].text
            
            # Extract JSON
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0]
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0]
            else:
                json_str = response_text
            
            batch_analysis = json.loads(json_str)
            
            # Merge with timeline data
            for j, analysis in enumerate(batch_analysis):
                if i + j < len(timeline):
                    merged = {
                        **timeline[i + j],
                        "analysis": analysis
                    }
                    all_analyses.append(merged)
                    
        except Exception as e:
            print(f"   ⚠️ Error in batch {batch_num}: {e}")
            # Add entries without analysis
            for entry in batch:
                all_analyses.append({**entry, "analysis": None})
    
    # Save analyses
    analyses_path = output_dir / "analyses.json"
    with open(analyses_path, "w") as f:
        json.dump(all_analyses, f, indent=2)
    
    print(f"✅ Analysis complete")
    return all_analyses


def build_knowledge_graph(analyses: list, software_name: str, output_dir: Path) -> dict:
    """Build knowledge graph from analyses"""
    print(f"\n🧠 Building knowledge graph...")
    
    import anthropic
    
    client = anthropic.Anthropic()
    
    # Prepare summary of analyses
    analysis_summary = json.dumps(analyses, indent=2)
    
    # Truncate if too long
    if len(analysis_summary) > 50000:
        analysis_summary = analysis_summary[:50000] + "\n... (truncated)"
    
    prompt = f"""Based on this analysis of a "{software_name}" demonstration video, create a comprehensive knowledge graph.

ANALYSIS DATA:
{analysis_summary}

Generate a JSON knowledge graph with this structure:

{{
  "software_name": "{software_name}",
  "extraction_date": "{datetime.now().isoformat()}",
  
  "modules": [
    {{"id": "module_id", "name": "Module Name", "description": "What it does"}}
  ],
  
  "features": [
    {{
      "id": "feature_id",
      "name": "Feature Name",
      "module": "module_id",
      "description": "What the feature does",
      "type": "create|read|update|delete|workflow|report",
      "user_steps": ["Step 1", "Step 2"],
      "screens_involved": ["screen_ids"],
      "business_value": "Why this feature matters"
    }}
  ],
  
  "screens": [
    {{
      "id": "screen_id",
      "name": "Screen Name",
      "module": "module_id",
      "purpose": "What users do here",
      "url_pattern": "/suggested/url",
      "components": [
        {{"type": "button|form|table|etc", "label": "Label", "action": "what it does"}}
      ],
      "navigates_to": ["other_screen_ids"],
      "navigates_from": ["other_screen_ids"]
    }}
  ],
  
  "user_flows": [
    {{
      "id": "flow_id",
      "name": "Flow Name",
      "description": "End-to-end user journey",
      "steps": [
        {{"sequence": 1, "screen": "screen_id", "action": "User does X", "result": "System shows Y"}}
      ]
    }}
  ],
  
  "business_processes": [
    {{
      "id": "process_id",
      "name": "Process Name",
      "description": "Business process description",
      "actors": ["role names"],
      "triggers": ["What starts this process"],
      "steps": [
        {{"sequence": 1, "name": "Step name", "type": "task|decision|event", "performer": "role"}}
      ],
      "outcomes": ["What this process produces"]
    }}
  ],
  
  "data_entities": [
    {{
      "id": "entity_id",
      "name": "Entity Name",
      "description": "What this data represents",
      "fields": [
        {{"name": "field_name", "type": "string|number|date|relation", "description": "What it stores"}}
      ],
      "relationships": [
        {{"type": "has_many|belongs_to", "target": "other_entity_id"}}
      ]
    }}
  ],
  
  "ui_patterns": {{
    "layout_type": "sidebar|topnav|etc",
    "color_scheme": "observed colors",
    "component_library": "if identifiable (Bootstrap, Material, etc)",
    "common_patterns": ["List pattern descriptions"]
  }}
}}

Extract ALL information visible in the demonstration. Be thorough."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Parse response
    response_text = response.content[0].text
    
    if "```json" in response_text:
        json_str = response_text.split("```json")[1].split("```")[0]
    elif "```" in response_text:
        json_str = response_text.split("```")[1].split("```")[0]
    else:
        json_str = response_text
    
    knowledge_graph = json.loads(json_str)
    
    # Save knowledge graph
    kg_path = output_dir / "knowledge_graph.json"
    with open(kg_path, "w") as f:
        json.dump(knowledge_graph, f, indent=2)
    
    print(f"✅ Knowledge graph saved to {kg_path}")
    return knowledge_graph


def generate_documentation(knowledge_graph: dict, output_dir: Path):
    """Generate markdown documentation from knowledge graph"""
    print(f"\n📝 Generating documentation...")
    
    kg = knowledge_graph
    software_name = kg.get("software_name", "Software")
    
    # User Manual
    manual = f"""# {software_name} User Manual

*Auto-generated from video demonstration*

## Overview

This documentation covers the features demonstrated in the {software_name} video.

## Modules

"""
    
    for module in kg.get("modules", []):
        manual += f"### {module['name']}\n\n{module.get('description', '')}\n\n"
    
    manual += "## Features\n\n"
    
    for feature in kg.get("features", []):
        manual += f"""### {feature['name']}

**Module**: {feature.get('module', 'N/A')}  
**Type**: {feature.get('type', 'N/A')}

{feature.get('description', '')}

**Steps**:
"""
        for i, step in enumerate(feature.get('user_steps', []), 1):
            manual += f"{i}. {step}\n"
        
        manual += f"\n**Business Value**: {feature.get('business_value', 'N/A')}\n\n---\n\n"
    
    manual += "## Screens\n\n"
    
    for screen in kg.get("screens", []):
        manual += f"""### {screen['name']}

**Purpose**: {screen.get('purpose', '')}

**Components**:
"""
        for comp in screen.get("components", []):
            manual += f"- **{comp.get('label', 'N/A')}** ({comp.get('type', '')}): {comp.get('action', '')}\n"
        
        manual += "\n---\n\n"
    
    # Save manual
    manual_path = output_dir / "USER_MANUAL.md"
    with open(manual_path, "w") as f:
        f.write(manual)
    
    # Process Documentation (BPMN-style)
    process_doc = f"""# {software_name} Business Processes

## Process Diagrams

"""
    
    for process in kg.get("business_processes", []):
        process_doc += f"""### {process['name']}

{process.get('description', '')}

**Actors**: {', '.join(process.get('actors', []))}

**Triggers**: {', '.join(process.get('triggers', []))}

**Process Steps**:

```
"""
        for step in process.get("steps", []):
            step_type = step.get("type", "task")
            if step_type == "decision":
                process_doc += f"  ◇ {step['name']} ({step.get('performer', '')})\n"
            elif step_type == "event":
                process_doc += f"  ○ {step['name']}\n"
            else:
                process_doc += f"  □ {step['name']} ({step.get('performer', '')})\n"
        
        process_doc += f"""```

**Outcomes**: {', '.join(process.get('outcomes', []))}

---

"""
    
    # Save process doc
    process_path = output_dir / "BUSINESS_PROCESSES.md"
    with open(process_path, "w") as f:
        f.write(process_doc)
    
    # UI Design Spec
    ui_doc = f"""# {software_name} UI Design Specification

## Layout & Patterns

"""
    
    ui_patterns = kg.get("ui_patterns", {})
    ui_doc += f"""**Layout Type**: {ui_patterns.get('layout_type', 'N/A')}
**Color Scheme**: {ui_patterns.get('color_scheme', 'N/A')}
**Component Library**: {ui_patterns.get('component_library', 'N/A')}

### Common Patterns

"""
    
    for pattern in ui_patterns.get("common_patterns", []):
        ui_doc += f"- {pattern}\n"
    
    ui_doc += "\n## Screen Specifications\n\n"
    
    for screen in kg.get("screens", []):
        ui_doc += f"""### {screen['name']}

**URL Pattern**: `{screen.get('url_pattern', '/unknown')}`

**Components**:
| Type | Label | Action |
|------|-------|--------|
"""
        for comp in screen.get("components", []):
            ui_doc += f"| {comp.get('type', '')} | {comp.get('label', '')} | {comp.get('action', '')} |\n"
        
        ui_doc += "\n---\n\n"
    
    # Save UI doc
    ui_path = output_dir / "UI_DESIGN_SPEC.md"
    with open(ui_path, "w") as f:
        f.write(ui_doc)
    
    print(f"✅ Documentation generated:")
    print(f"   - {manual_path}")
    print(f"   - {process_path}")
    print(f"   - {ui_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract software documentation from YouTube demo videos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python extract.py "https://youtube.com/watch?v=xyz" --name "Odoo CRM"
  python extract.py "https://youtube.com/watch?v=abc" --name "SAP" --whisper-model large
  python extract.py "https://youtube.com/watch?v=def" --skip-transcription
        """
    )
    
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--name", "-n", default="Software", help="Name of the software being demonstrated")
    parser.add_argument("--output", "-o", default="./output", help="Output directory")
    parser.add_argument("--interval", "-i", type=int, default=5, help="Screenshot interval in seconds (default: 5)")
    parser.add_argument("--whisper-model", "-w", default="base", 
                       choices=["tiny", "base", "small", "medium", "large"],
                       help="Whisper model size (default: base)")
    parser.add_argument("--skip-transcription", action="store_true", 
                       help="Skip audio transcription")
    parser.add_argument("--skip-analysis", action="store_true",
                       help="Skip AI analysis (just extract frames and audio)")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🎬 Software Feature Extractor")
    print("=" * 60)
    print(f"Video: {args.url}")
    print(f"Software: {args.name}")
    print(f"Output: {args.output}")
    print("=" * 60)
    
    # Check dependencies
    check_dependencies()
    
    # Setup output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Download video
    video_path = download_video(args.url, output_dir)
    
    # Step 2: Extract frames
    frames = extract_frames(video_path, output_dir, args.interval)
    
    # Step 3: Extract and transcribe audio
    if not args.skip_transcription:
        audio_path = extract_audio(video_path, output_dir)
        transcript = transcribe_audio(audio_path, output_dir, args.whisper_model)
    else:
        transcript = {"full_text": "", "segments": []}
    
    # Step 4: Create timeline
    timeline = create_timeline(frames, transcript, output_dir)
    
    if args.skip_analysis:
        print("\n⏭️ Skipping AI analysis (--skip-analysis)")
        print(f"\n✅ Basic extraction complete! Check {output_dir}")
        return
    
    # Step 5: Analyze with Claude
    analyses = analyze_with_claude(timeline, args.name, output_dir)
    
    # Step 6: Build knowledge graph
    knowledge_graph = build_knowledge_graph(analyses, args.name, output_dir)
    
    # Step 7: Generate documentation
    generate_documentation(knowledge_graph, output_dir)
    
    print("\n" + "=" * 60)
    print("🎉 Extraction Complete!")
    print("=" * 60)
    print(f"\nOutputs in {output_dir}/:")
    print("  📁 frames/           - Screenshots every 5 seconds")
    print("  📄 transcript.json   - Audio transcription")
    print("  📄 timeline.json     - Synced frames + transcript")
    print("  📄 analyses.json     - AI analysis of each frame")
    print("  📄 knowledge_graph.json - Complete knowledge graph")
    print("  📄 USER_MANUAL.md    - Generated user documentation")
    print("  📄 BUSINESS_PROCESSES.md - Process documentation")
    print("  📄 UI_DESIGN_SPEC.md - UI specifications")
    print("\n💡 Use knowledge_graph.json with Claude to generate code!")


if __name__ == "__main__":
    main()
