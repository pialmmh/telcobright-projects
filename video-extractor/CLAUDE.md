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
