# Claude Code CLI Agent Instructions

## Project: Software Feature Extractor

This project extracts knowledge graphs, documentation, and UI specifications from YouTube software demonstration videos (e.g., ERP/CRM demos).

---

## Project Structure

```
video-extractor/
├── extract.py          # Main extraction script (video → knowledge graph)
├── manual_input.py     # Convert YAML → knowledge graph (no video needed)
├── template.yaml       # YAML template for manual documentation
├── requirements.txt    # Python dependencies
└── README.md           # User documentation
```

---

## Current State

The project has a working MVP that:
1. Downloads YouTube videos via yt-dlp
2. Extracts frames every N seconds via FFmpeg
3. Transcribes audio via OpenAI Whisper (local)
4. Analyzes frames + transcript via Claude API
5. Builds a knowledge graph JSON
6. Generates markdown documentation

---

## Multi-Video Project Extraction

For multi-video ERP documentation projects, use:

```bash
python extract_project.py ./erp-1-docs/config.yaml
```

This processes videos organized by module/chapter and creates:
- `screenshots/` - frames per module
- `transcripts/` - whisper transcripts
- `timelines/` - **frames mapped to transcript descriptions**

---

## Vertical Scroll Detection (IMPORTANT)

When analyzing consecutive frames, detect if they show the **same screen scrolled vertically**. This is critical for:
- Long forms with many fields
- Data tables/grids
- Reports and lists
- Configuration pages

### Detection Strategy

1. **Compare UI Header/Navigation**: If top navigation bar, page title, or breadcrumbs are identical → likely same screen
2. **Compare Fixed Elements**: Sidebars, footers, action buttons that stay fixed during scroll
3. **Detect Overlapping Content**: If bottom portion of frame N matches top portion of frame N+1 → vertical scroll
4. **Check URL/Tab Indicators**: If visible URL bar or tab title is the same → same screen

### Implementation Approach

When Claude analyzes frames, include this in the prompt:

```
For each frame, determine:
1. screen_id: Unique identifier for this screen (e.g., "customer_list", "order_form")
2. is_scroll_continuation: true if this frame shows the same screen as previous frame, just scrolled
3. scroll_position: "top", "middle", "bottom" if determinable
4. visible_section: What part of the screen is visible (e.g., "form fields 1-10", "table rows 50-100")
```

### Timeline Grouping

When `is_scroll_continuation: true`, group frames together:

```json
{
  "screen_id": "customer_form",
  "screen_name": "Customer Edit Form",
  "frames": [
    {
      "frame_path": "frame_0001.jpg",
      "timestamp": "00:00",
      "scroll_position": "top",
      "visible_section": "Basic Info fields",
      "description": "Now we'll fill in the customer details..."
    },
    {
      "frame_path": "frame_0002.jpg",
      "timestamp": "05:00",
      "scroll_position": "middle",
      "visible_section": "Address fields",
      "description": "Scrolling down to the address section..."
    },
    {
      "frame_path": "frame_0003.jpg",
      "timestamp": "10:00",
      "scroll_position": "bottom",
      "visible_section": "Contact and Notes fields",
      "description": "At the bottom we have contact preferences..."
    }
  ],
  "combined_description": "Complete customer form with Basic Info, Address, and Contact sections..."
}
```

### Benefits

- **Accurate Screen Count**: Don't count scrolled views as separate screens
- **Complete UI Documentation**: Combine all visible fields/components from scroll sequence
- **Better Knowledge Graph**: One node per logical screen, not per frame

---

## Next Tasks (Priority Order)

### 1. Add Neo4j Export for Knowledge Graph

**Goal**: Export the knowledge graph to Neo4j for graph database storage and querying.

**File to create**: `export_neo4j.py`

**Requirements**:
```bash
pip install neo4j
```

**Implementation hints**:
```python
from neo4j import GraphDatabase

def export_to_neo4j(kg_path: str, uri: str, user: str, password: str):
    """
    Create nodes: Module, Feature, Screen, Component, Actor, Process, Entity
    Create relationships: BELONGS_TO, HAS_SCREEN, HAS_COMPONENT, NAVIGATES_TO, etc.
    """
    pass
```

**Test command**:
```bash
python export_neo4j.py ./output/knowledge_graph.json --uri bolt://localhost:7687
```

---

### 2. Add BPMN 2.0 XML Export

**Goal**: Generate valid BPMN 2.0 XML files that can be opened in Camunda Modeler, bpmn.io, etc.

**File to create**: `export_bpmn.py`

**The current code in the architecture doc has a basic implementation. Enhance it to**:
- Add proper BPMN DI (diagram interchange) for visual layout
- Support lanes for different actors
- Support gateways (exclusive, parallel)
- Support events (start, end, intermediate)

**Test**: Open output in https://demo.bpmn.io/

---

### 3. Add React Component Generator

**Goal**: Generate React components from the UI specifications in the knowledge graph.

**File to create**: `generate_react.py`

**Implementation approach**:
```python
def generate_react_component(screen: dict, design_system: dict) -> str:
    """
    Given a screen definition from knowledge_graph.json,
    generate a React functional component with:
    - Proper imports
    - Tailwind CSS styling based on design_system
    - Component structure matching the screen's components list
    - Basic state management for forms
    - Navigation hooks for screen transitions
    """
    pass
```

**Output structure**:
```
output/react-components/
├── CustomerList.jsx
├── CustomerDetail.jsx
├── OrderForm.jsx
└── components/
    ├── Button.jsx
    ├── Table.jsx
    └── Form.jsx
```

---

### 4. Add OpenAPI/Swagger Generation

**Goal**: Generate OpenAPI 3.0 specs from the data entities and features.

**File to create**: `generate_openapi.py`

**Should produce**:
- CRUD endpoints for each entity
- Request/response schemas from entity fields
- Path parameters from relationships
- Tags organized by module

---

### 5. Add Database Schema Generation

**Goal**: Generate SQL DDL or Prisma schema from data entities.

**File to create**: `generate_schema.py`

**Output formats to support**:
- PostgreSQL DDL
- MySQL DDL
- Prisma schema
- TypeORM entities

---

### 6. Improve Frame Analysis with OCR

**Goal**: Extract text from screenshots more accurately using dedicated OCR.

**Implementation**:
- Add Tesseract OCR as preprocessing step
- Extract all visible text from each frame
- Include OCR results in the analysis prompt for better accuracy

**Install**: `pip install pytesseract` + Tesseract binary

---

### 7. Add Support for Alternative STT Services

**Goal**: Allow users to choose between Whisper, AssemblyAI, or Deepgram.

**Modify**: `extract.py`

**Add argument**:
```bash
python extract.py "URL" --stt whisper|assemblyai|deepgram
```

**Implementation**: The architecture document has code for all three services.

---

### 8. Add Interactive Mode

**Goal**: Allow users to review and correct the AI analysis interactively.

**File to create**: `interactive_review.py`

**Features**:
- Show each frame with its analysis
- Allow user to edit/correct screen names, features, etc.
- Save corrections back to analyses.json
- Re-generate knowledge graph with corrections

---

### 9. Add Batch Processing

**Goal**: Process multiple videos and merge into a single knowledge graph.

**File to create**: `batch_extract.py`

**Usage**:
```bash
python batch_extract.py videos.txt --name "Complete ERP Documentation"
```

Where `videos.txt` contains one YouTube URL per line.

---

### 10. Add Web UI

**Goal**: Create a simple web interface for the extraction process.

**Tech stack**: FastAPI + React or Streamlit

**Features**:
- Paste YouTube URL
- Configure options (interval, whisper model, etc.)
- Show progress
- Display results with frame viewer
- Edit/export knowledge graph

---

## Code Quality Improvements

### Add Type Hints
All functions should have proper type hints:
```python
def analyze_screenshot_batch(
    client: anthropic.Anthropic,
    screenshots: list[dict],
    software_context: str
) -> list[dict]:
```

### Add Error Handling
Wrap API calls and file operations in try/except with meaningful error messages.

### Add Logging
Replace `print()` with proper logging:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### Add Tests
Create `tests/` directory with:
- `test_extract.py` - Unit tests for extraction functions
- `test_knowledge_graph.py` - Validate KG structure
- `test_generators.py` - Test output generators

---

## Environment Setup

```bash
# Clone/download the project
cd video-extractor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install system dependencies
# Mac: brew install ffmpeg tesseract
# Ubuntu: sudo apt install ffmpeg tesseract-ocr

# Set API key
export ANTHROPIC_API_KEY="your-key"
```

---

## Testing Commands

```bash
# Test with a short video (< 5 min recommended for testing)
python extract.py "https://www.youtube.com/watch?v=VIDEO_ID" --name "Test" --interval 10

# Test manual input
python manual_input.py template.yaml --output ./test-output

# Test with skip options (faster)
python extract.py "URL" --name "Test" --skip-transcription --skip-analysis
```

---

## Key Files to Understand

1. **extract.py** - Main entry point. Read `main()` and follow the pipeline:
   - `download_video()` → `extract_frames()` → `extract_audio()` → `transcribe_audio()`
   - `create_timeline()` → `analyze_with_claude()` → `build_knowledge_graph()`
   - `generate_documentation()`

2. **knowledge_graph.json** - The core output format. All generators consume this.

3. **template.yaml** - The schema for manual input. Extend this for new entity types.

---

## API Usage Notes

### Claude API
- Uses `claude-sonnet-4-20250514` for analysis (good balance of speed/quality)
- Batch size of 5 frames per API call to manage context window
- Images sent as base64-encoded JPEG

### Whisper
- Default model is "base" (good balance)
- Use "large" for better accuracy on technical content
- Runs locally, no API key needed

---

## Common Issues

| Issue | Solution |
|-------|----------|
| FFmpeg not found | Install: `brew install ffmpeg` or `apt install ffmpeg` |
| yt-dlp fails | Update: `pip install --upgrade yt-dlp` |
| Whisper OOM | Use smaller model: `--whisper-model tiny` |
| Claude API error | Check API key, check rate limits |
| JSON parse error | Claude sometimes returns malformed JSON; add retry logic |

---

## Architecture Decisions

1. **Why local Whisper vs cloud STT?** 
   - Free, no API key needed, good enough for most videos
   - Cloud options (AssemblyAI, Deepgram) available for better accuracy

2. **Why Claude vs GPT-4V?**
   - Claude has larger context window for batching frames
   - Better at structured JSON output
   - Can switch to GPT-4V by changing the API calls

3. **Why JSON-LD for knowledge graph?**
   - Standard format, interoperable
   - Can be loaded into graph databases
   - Easy to extend with custom ontology

---

## Extending the Knowledge Graph Schema

To add new entity types, modify:

1. `build_knowledge_graph()` prompt in `extract.py`
2. Add corresponding section in `template.yaml`
3. Update `generate_documentation()` to handle new type
4. Add new generator if needed (e.g., `generate_X.py`)

---

## Contact / Resources

- Anthropic API docs: https://docs.anthropic.com/
- Whisper: https://github.com/openai/whisper
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- BPMN 2.0 spec: https://www.omg.org/spec/BPMN/2.0/
