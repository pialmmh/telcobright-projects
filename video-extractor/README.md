# 🎬 Software Feature Extractor

Extract knowledge graphs, documentation, and UI specs from YouTube software demonstration videos.

## What This Does

1. **Downloads** a YouTube video
2. **Captures screenshots** every 5 seconds
3. **Transcribes audio** using OpenAI Whisper (free, runs locally)
4. **Analyzes** each screenshot + transcript with Claude AI
5. **Generates** a knowledge graph + documentation

## Output Files

```
output/
├── frames/                  # Screenshots every 5 seconds
├── video.mp4               # Downloaded video
├── audio.wav               # Extracted audio
├── transcript.json         # Speech-to-text result
├── timeline.json           # Frames synced with transcript
├── analyses.json           # AI analysis of each frame
├── knowledge_graph.json    # ⭐ The main output - use this!
├── USER_MANUAL.md          # Generated user documentation
├── BUSINESS_PROCESSES.md   # BPMN-style process docs
└── UI_DESIGN_SPEC.md       # UI component specifications
```

---

## 🚀 Quick Start

### Step 1: Install System Dependencies

**Mac:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from https://ffmpeg.org/download.html and add to PATH.

### Step 2: Install Python Packages

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Set Your Anthropic API Key

```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

Get a key at: https://console.anthropic.com/

### Step 4: Run!

```bash
python extract.py "https://www.youtube.com/watch?v=VIDEO_ID" --name "Software Name"
```

---

## 📖 Usage Examples

### Basic Usage
```bash
python extract.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --name "Odoo CRM"
```

### Specify Output Directory
```bash
python extract.py "https://youtu.be/xyz" --name "SAP" --output ./sap-docs
```

### Use Larger Whisper Model (Better Accuracy)
```bash
python extract.py "URL" --name "Software" --whisper-model large
```

Whisper model options:
- `tiny` - Fastest, least accurate
- `base` - Good balance (default)
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy, slowest

### Change Screenshot Interval
```bash
# Capture every 3 seconds (more detail)
python extract.py "URL" --name "Software" --interval 3

# Capture every 10 seconds (faster processing)
python extract.py "URL" --name "Software" --interval 10
```

### Skip Transcription (Faster)
```bash
python extract.py "URL" --name "Software" --skip-transcription
```

### Just Extract Frames (No AI)
```bash
python extract.py "URL" --name "Software" --skip-analysis
```

---

## 💡 Using the Knowledge Graph

The `knowledge_graph.json` file is structured for AI consumption. Use it with Claude to:

### Generate Code
```
Based on this knowledge graph, generate a React component for the 
"Customer List" screen with the specified components and layout.

[paste knowledge_graph.json]
```

### Create More Documentation
```
Using this knowledge graph, create detailed API specifications 
for the backend services that would support these features.

[paste knowledge_graph.json]
```

### Build a Clone
```
I want to build a similar application. Using this knowledge graph,
create a complete project plan with database schema, API endpoints,
and frontend components.

[paste knowledge_graph.json]
```

---

## 🔧 Troubleshooting

### "ffmpeg not found"
Install ffmpeg for your OS (see Step 1).

### "yt-dlp error"
Update yt-dlp: `pip install --upgrade yt-dlp`

### "ANTHROPIC_API_KEY not set"
Export your key: `export ANTHROPIC_API_KEY="your-key"`

### "Whisper out of memory"
Use a smaller model: `--whisper-model tiny` or `--whisper-model base`

### Video download fails
- Check if the video is public
- Try updating yt-dlp
- Some videos may be geo-restricted

---

## 📊 Cost Estimate

- **Whisper**: Free (runs locally)
- **Claude API**: ~$0.50-2.00 per video (depends on length)
  - ~$0.003 per 1K input tokens
  - ~$0.015 per 1K output tokens
  - A 10-minute video ≈ 120 frames ≈ 24 API calls

---

## 🤝 Tips for Best Results

1. **Choose clear demo videos** - Official tutorials work best
2. **Avoid music/noise** - Clean audio = better transcription
3. **Standard UI patterns** - The AI recognizes common ERP/CRM layouts
4. **English audio** - Whisper works best with English

---

## License

MIT - Use freely for any purpose.
