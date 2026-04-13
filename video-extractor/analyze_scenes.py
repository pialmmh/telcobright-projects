#!/usr/bin/env python3
"""
Analyze deduplicated scenes with Claude.
- Sonnet: per-scene analysis + CC extraction + CRM/calling filter
- Opus: final knowledge graph build
"""

import os
import sys
import json
import base64
import logging
from pathlib import Path
from datetime import datetime

# Load .env
env_file = Path(".env")
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ[k.strip()] = v.strip()

import anthropic

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

FOLDER = sys.argv[1] if len(sys.argv) > 1 else "crm-mightycall"
SCENES_JSON = Path(FOLDER) / "scenes.json"
OUTPUT_DIR  = Path(FOLDER)
ANALYSES_JSON = OUTPUT_DIR / "analyses.json"

SONNET = "claude-sonnet-4-5"
OPUS   = "claude-opus-4-5"

client = anthropic.Anthropic()


def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode()


def analyze_batch(batch: list, batch_num: int, total: int) -> list:
    log.info(f"Batch {batch_num}/{total} — {len(batch)} scenes")

    content = []
    for scene in batch:
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": encode_image(scene["representative_path"])
            }
        })
        content.append({
            "type": "text",
            "text": f"[Scene {scene['scene_index']} | {scene['start_fmt']}–{scene['end_fmt']} | {scene['duration_sec']}s]"
        })

    content.append({
        "type": "text",
        "text": f"""You are analyzing screenshots from a MightyCall CRM / dialer demo video (topic: {FOLDER}).

For EACH screenshot (in order), return a JSON object with:
- "scene_index": integer (from the label above)
- "caption_text": extract any visible closed-caption / subtitle text from the bottom of the screen (empty string if none)
- "is_crm_calling_related": true if screen shows CRM or calling features (dialer, contacts, campaigns, call logs, IVR, agent dashboard, click-to-call, recordings, leads, deals). false for ads, sponsor segments, generic UI, presenter face, intro/outro slides.
- "screen_name": name of the screen/page shown
- "module": which module (Predictive Dialer, Preview Dialer, Progressive Dialer, Campaign, Contact, Call Log, IVR, Dashboard, etc.)
- "feature_demonstrated": specific feature being shown
- "user_action": what the user is doing
- "ui_components": array of {{type, label, purpose}}
- "data_fields": visible form fields or table columns
- "navigation_context": where this fits in the user journey
- "business_process": what business process this supports

Return ONLY a JSON array, one object per screenshot, no other text."""
    })

    response = client.messages.create(
        model=SONNET,
        max_tokens=4000,
        messages=[{"role": "user", "content": content}]
    )

    text = response.content[0].text
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0]
    elif "```" in text:
        text = text.split("```")[1].split("```")[0]

    return json.loads(text)


def run_analysis(scenes: list) -> list:
    # Resume: skip already-analyzed scenes
    existing = {}
    if ANALYSES_JSON.exists():
        for a in json.loads(ANALYSES_JSON.read_text()):
            existing[a["scene_index"]] = a
        log.info(f"Resuming — {len(existing)} scenes already done")

    remaining = [s for s in scenes if s["scene_index"] not in existing]
    log.info(f"Scenes to analyze: {len(remaining)}")

    batch_size = 5
    for i in range(0, len(remaining), batch_size):
        batch = remaining[i:i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(remaining) + batch_size - 1) // batch_size

        try:
            results = analyze_batch(batch, batch_num, total_batches)
            for r in results:
                # Merge scene metadata into analysis
                scene = next(s for s in batch if s["scene_index"] == r["scene_index"])
                existing[r["scene_index"]] = {**scene, "analysis": r}
        except Exception as e:
            log.warning(f"Batch {batch_num} failed: {e}")
            for s in batch:
                existing[s["scene_index"]] = {**s, "analysis": None}

        # Save after every batch (safe to resume)
        all_analyses = [existing[k] for k in sorted(existing)]
        ANALYSES_JSON.write_text(json.dumps(all_analyses, indent=2))

    all_analyses = [existing[k] for k in sorted(existing)]
    crm_count = sum(1 for a in all_analyses
                    if a.get("analysis") and a["analysis"].get("is_crm_calling_related"))
    log.info(f"Done. {crm_count}/{len(all_analyses)} scenes are CRM/calling related")
    return all_analyses


def build_knowledge_graph(analyses: list) -> dict:
    log.info("Building knowledge graph with Opus...")

    # Filter to CRM/calling scenes only
    relevant = [a for a in analyses
                if a.get("analysis") and a["analysis"].get("is_crm_calling_related")]
    log.info(f"Using {len(relevant)} relevant scenes for knowledge graph")

    # Aggregate captions as narration context
    narration = " ".join(
        a["analysis"].get("caption_text", "")
        for a in relevant
        if a["analysis"].get("caption_text")
    )

    summary = json.dumps([a["analysis"] for a in relevant], indent=2)
    if len(summary) > 60000:
        summary = summary[:60000] + "\n...(truncated)"

    prompt = f"""You are building a structured knowledge graph of MightyCall's CRM and dialer features (source: {FOLDER}).

SCENE ANALYSES (from {len(relevant)} screens):
{summary}

NARRATION (from closed captions):
{narration[:5000]}

Generate a comprehensive knowledge graph as JSON. Include ONLY features related to CRM and calling (predictive dialer, campaigns, contacts, call logs, IVR, agent dashboard, recordings, click-to-call, leads). Discard anything unrelated.

Structure:
{{
  "software_name": "MightyCall",
  "source_video": "{FOLDER}",
  "extraction_date": "{datetime.now().isoformat()}",
  "modules": [{{"id", "name", "description"}}],
  "features": [{{
    "id", "name", "module", "description",
    "type": "create|read|update|delete|workflow|report|configuration",
    "user_steps": [],
    "business_value": ""
  }}],
  "screens": [{{
    "id", "name", "module", "purpose", "url_pattern",
    "components": [{{"type", "label", "action"}}],
    "navigates_to": [], "navigates_from": []
  }}],
  "user_flows": [{{
    "id", "name", "description",
    "steps": [{{"sequence", "screen", "action", "result"}}]
  }}],
  "business_processes": [{{
    "id", "name", "description", "actors": [],
    "triggers": [],
    "steps": [{{"sequence", "name", "type", "performer"}}],
    "outcomes": []
  }}],
  "data_entities": [{{
    "id", "name", "description",
    "fields": [{{"name", "type", "description"}}],
    "relationships": [{{"type", "target"}}]
  }}],
  "ui_patterns": {{
    "layout_type", "color_scheme", "component_library", "common_patterns": []
  }}
}}

Be thorough. Return ONLY valid JSON."""

    response = client.messages.create(
        model=OPUS,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.content[0].text
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0]
    elif "```" in text:
        text = text.split("```")[1].split("```")[0]

    kg = json.loads(text)
    kg_path = OUTPUT_DIR / "knowledge_graph.json"
    kg_path.write_text(json.dumps(kg, indent=2))
    log.info(f"Knowledge graph saved to {kg_path}")
    return kg


def generate_docs(kg: dict):
    from extract import generate_documentation
    generate_documentation(kg, OUTPUT_DIR)


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set")
        exit(1)

    scenes = json.loads(SCENES_JSON.read_text())
    log.info(f"[{FOLDER}] Loaded {len(scenes)} scenes")

    analyses = run_analysis(scenes)
    kg = build_knowledge_graph(analyses)

    # Generate markdown docs
    try:
        from extract import generate_documentation
        generate_documentation(kg, OUTPUT_DIR)
    except Exception as e:
        log.warning(f"Doc generation skipped: {e}")

    log.info(f"All done. Outputs in {FOLDER}/")
