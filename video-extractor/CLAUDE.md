# CLAUDE.md - Project Context for Claude Code CLI

## What is this project?

A tool that extracts software documentation and knowledge graphs from YouTube demonstration videos. It captures screenshots, transcribes audio, analyzes UI with Claude AI, and generates structured outputs for AI-driven development.

## Quick Commands

```bash
# Run extraction on a video
python extract.py "YOUTUBE_URL" --name "Software Name"

# Manual input (no video)
python manual_input.py template.yaml

# Install dependencies
pip install -r requirements.txt
```

## Project Files

| File | Purpose |
|------|---------|
| `extract.py` | Main pipeline: video → knowledge graph |
| `manual_input.py` | YAML → knowledge graph converter |
| `template.yaml` | Schema for manual documentation |
| `requirements.txt` | Python dependencies |
| `CLAUDE_CODE_INSTRUCTIONS.md` | Detailed dev instructions |

## Output Files (in ./output/)

| File | Purpose |
|------|---------|
| `knowledge_graph.json` | **Main output** - structured software knowledge |
| `USER_MANUAL.md` | Generated user documentation |
| `BUSINESS_PROCESSES.md` | BPMN-style process docs |
| `UI_DESIGN_SPEC.md` | UI component specifications |
| `timeline.json` | Frames synced with transcript |
| `analyses.json` | Per-frame AI analysis |

## Key Dependencies

- `yt-dlp` - YouTube download
- `ffmpeg` - Frame/audio extraction
- `openai-whisper` - Speech-to-text (local)
- `anthropic` - Claude API for analysis

## Environment Variables

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Current TODO (pick one to work on)

1. **Neo4j export** - Export knowledge graph to graph database
2. **BPMN 2.0 export** - Generate valid BPMN XML with diagram layout
3. **React generator** - Generate React components from UI specs
4. **OpenAPI generator** - Generate API specs from entities
5. **Database schema** - Generate SQL/Prisma from entities

See `CLAUDE_CODE_INSTRUCTIONS.md` for detailed specs on each task.

---

## Tutorial Screenshot → Karpathy Wiki Process

This is the standard workflow used to build knowledge wikis from YouTube tutorials. Follow exactly.

### Step 1 — Screen Capture

User plays the YouTube tutorial in a browser **with captions ON**. Claude runs:

```bash
cd /home/mustafa/telcobright-projects/video-extractor
./capture.sh <product-name> <duration-seconds>
# Example: ./capture.sh espocrm 1020   (17 min = 1020 sec)
```

Frames land in `./<product-name>/frames/frame_NNNN.jpg` at 1 fps.
Tell the user "go" so they start playing and start the script immediately after.

### Step 2 — Deduplicate Frames

```bash
cd /home/mustafa/telcobright-projects/video-extractor
python dedupe_frames.py <product-name>
```

This writes `<product-name>/scenes.json` — an array of scenes. Each scene has fields:
- `scene_id`, `representative_frame`, `start_frame`, `end_frame`, `duration_sec`

Filter to scenes with `duration_sec >= 5` to skip UI transitions. These are "significant scenes".

### Step 3 — Read Frames Locally (No API Cost)

**Do NOT call any external API for frame analysis.** Use the `Read` tool to read each frame image locally — Claude can see the image content directly.

- Read frames in batches of ~10 at a time
- For each frame: note visible UI elements, field names, workflows, navigation, data shown
- Identify and discard: ads, intro slides, presenter talking-head with no UI, outro/contact info
- Focus on: screens, forms, data tables, settings panels, workflow steps

### Step 4 — Build `knowledge_graph.json`

After reading all significant scenes, write `<product-name>/knowledge_graph.json` with this structure:

```json
{
  "product": "EspoCRM",
  "source_video": "<product-name>/frames/",
  "total_scenes_analyzed": N,
  "discarded_scenes": [
    {"frames": "XXXX-XXXX", "reason": "ad / intro / off-topic"}
  ],
  "modules": [
    {
      "name": "ModuleName",
      "navigation_path": "Top Nav > Sub Menu",
      "features": ["feature1", "feature2"],
      "screens": [
        {
          "name": "Screen Name",
          "description": "What this screen does",
          "components": ["table", "form", "panel"],
          "fields": [{"name": "field_name", "type": "text|dropdown|etc", "notes": ""}]
        }
      ]
    }
  ],
  "data_entities": [
    {
      "name": "EntityName",
      "fields": [{"name": "field_name", "type": "type", "notes": ""}],
      "relationships": ["Entity → has many → OtherEntity"]
    }
  ],
  "ui_patterns": {
    "layout": "",
    "color_scheme": {},
    "navigation": {}
  },
  "cross_module_features": []
}
```

### Step 5 — Write Karpathy-Style Wiki Pages

Wiki pages go in `wiki/` directory. Follow the format in `Contact_Center/docs/karpathy-wiki-guide.md` exactly.

**Naming convention**: `<product>-<topic>.md` e.g. `espocrm-leads.md`, `espocrm-data-entities.md`

**Mandatory files per product added to wiki**:
- One overview/modules page: `<product>-modules.md`
- One data entities page: `<product>-data-entities.md`
- One page per major module/feature (if >30 lines of content)

**Every page must have**:
```markdown
# Page Title

One sentence describing what this page covers and why it matters.

**Source**: `<product>/knowledge_graph.json`

## Section Heading
...

## See Also
- [related-page.md](related-page.md) — description
```

**After writing all pages**:
1. Update `wiki/index.md` — add new product section with links to all new pages
2. Update `wiki/log.md` — add dated entry (newest at top) listing: sources ingested, pages created, key observations, discarded scenes

### Step 6 — Reference existing wiki as format baseline

- Dialer wiki pages (`campaign-management.md`, `dialing-modes.md`, etc.) = format reference for feature/settings pages
- Salesforce pages (`salesforce-leads.md`, `salesforce-data-entities.md`, etc.) = format reference for CRM entity/module pages
- Use tables for field listings, state machines, comparisons
- Use code blocks for navigation paths and entity relationship trees

### Folder Layout After Completion

```
video-extractor/
├── <product-name>/
│   ├── frames/           ← raw 1fps screenshots
│   ├── scenes.json       ← deduplicated scene list
│   └── knowledge_graph.json
└── wiki/
    ├── index.md          ← updated with new product section
    ├── log.md            ← updated with new ingest entry
    └── <product>-*.md    ← new wiki pages
```

## Code Style

- Python 3.10+
- Type hints on all functions
- Use `logging` instead of `print()` for new code
- Handle errors gracefully with try/except

## Testing

```bash
# Quick test (skip AI analysis)
python extract.py "URL" --name "Test" --skip-analysis

# Full test with short video
python extract.py "URL" --name "Test" --interval 10 --whisper-model tiny
```
