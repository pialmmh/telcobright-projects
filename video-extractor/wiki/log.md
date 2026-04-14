# Ingest Log

## 2026-04-13: Salesforce Sales Cloud wiki added

**Source ingested:**
- `salesforce-crm/knowledge_graph.json` — Salesforce Sales Cloud tutorial (~40 min, 81 significant scenes of 353 total)

**Pages created:** 7
- salesforce-modules.md, salesforce-leads.md, salesforce-opportunities.md, salesforce-cases.md, salesforce-activities.md, salesforce-campaigns.md, salesforce-reports.md, salesforce-data-entities.md

**Key observations:**
- Full CRM module coverage: Leads, Accounts, Contacts, Opportunities, Cases, Tasks, Calendar, Reports, Dashboards, Campaigns
- Lead Conversion flow: one action creates Account + Contact + Opportunity simultaneously
- Opportunity pipeline: Qualification (20%) → Proposal/Price Quote (65%) → Negotiation/Review (75%) → Closed Won (100%) or Closed Lost
- Case detail: tri-panel layout (Case Details + Contact, Feed/Details center, Knowledge right)
- Kanban views available on Leads (by Status) and Opportunities (by Stage)
- Campaign ROI tracking via Primary Campaign Source field on Opportunities
- Dashboard "Sales Pipeline": 6 widgets, header KPI £210,800

**Discarded scenes:**
- Ads: Domestika (scenes 125-127), Hostinger (scene 214), Firebase (scene 259), Grammarly (scenes 304, 307, 312), Namecheap (scene 347)
- Presenter intro/outro

**Index updated:** Added Salesforce section to index.md

---

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
