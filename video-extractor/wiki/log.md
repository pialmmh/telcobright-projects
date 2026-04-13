# Ingest Log

## 2026-04-13: Initial wiki compilation

**Sources ingested:**
1. `crm-mightycall/knowledge_graph.json` — Predictive Dialer tutorial (8:00, 15 CRM scenes)
2. `preview-dialer/knowledge_graph.json` — Preview Dialer tutorial (6:18, 21 CRM scenes)
3. `progressive-dialer/knowledge_graph.json` — Progressive Dialer tutorial (6:52, 19 CRM scenes)

**Pages created:** 12
- index.md, campaign-management.md, dialing-modes.md, general-settings.md, dialer-settings.md, dispositions.md, dnc-compliance.md, local-presence.md, record-lists.md, agent-management.md, campaign-statuses.md, data-entities.md, ui-patterns.md, log.md

**Key decisions:**
- Merged overlapping content (campaign wizard steps identical across all 3 videos)
- Separated mode-specific dialer settings into comparison tables
- DNC compliance consolidated from all 3 sources (identical feature shown in each)
- Agent workspace documented from Preview + Progressive videos (not shown in Predictive video)
- Discarded non-CRM scenes: ads (GMass, Namecheap), intro slides, outro/contact info

**Discarded scenes:**
- crm-mightycall scenes 15-74: GMass email marketing ad
- preview-dialer scenes 21-26: outro, contact info, Namecheap ad
- progressive-dialer scenes 19-23: outro, contact info, MightyCall logo, black screen
