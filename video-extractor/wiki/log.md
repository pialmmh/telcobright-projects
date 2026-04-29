# Ingest Log

## 2026-04-29: Odoo 17 Product Management wiki added

**Source**: `odoo/product/screenshots/` — 15:00 demo "How to Manage Products in Odoo 17", captured at 1 fps (900 frames → 670 scenes → 38 ≥3s → 19 kept) on `runbot134.odoo.com` using a focused-window screen grab

**Pages created**: 7
- odoo-product-modules.md, odoo-product-general.md, odoo-product-variants.md, odoo-product-sales.md, odoo-product-purchase.md, odoo-product-inventory.md, odoo-product-update-quantity.md, odoo-product-data-entities.md

**Key observations**:
- Single Product form with 7 tabs (General Information / Attributes & Variants / Sales / Purchase / Inventory / Accounting / eBay) — only the first 5 demoed
- Product Type has 8 values: Consumable, Service, Storable Product, Booking Fees, Combo, Event Ticket, Event Booth, Course
- Sales tab is wider than expected — covers eCommerce categories, Self-Order/Kiosk description, POS visibility, and three flavours of cross-sell (Optional / Accessory / Alternative)
- Variants smart button only appears after Attributes & Variants is saved with values; count badge is the cartesian product of selected values
- Update Quantity is the canonical UX for stock adjustment per-variant per-location, reachable via smart-button on the product form
- Captured with new `capture-window.sh` (focused-window x11grab) instead of full-screen `capture.sh`

**Discarded scenes**:
- 0001-0068 (intro / channel branding before any UI)
- 0070-0133, 0135-0216, 0250-0345, 0500-0593 (narration-only over screens already captured by their representative frame)
- 0840-0900 (outro / call to subscribe)

**Tooling note**: lowered the "significant scene" threshold from 5s to 3s for this video — Odoo's UI has heavy mouse motion that fragments scenes via phash drift, so the default ≥5s filter dropped real content.

---

## 2026-04-28: InterCloud9 Predictive Dialer wiki added

**Source ingested:**
- `intercloud9-dialer/knowledge_graph.json` — InterCloud9 Predictive Dialer demo (4:40, 17 significant scenes of 54 total, from 280 captured frames at `pd.intercloud9.com`)

**Pages created:** 8
- intercloud9-modules.md, intercloud9-agent-home.md, intercloud9-contact-view.md, intercloud9-campaigns.md, intercloud9-agent-monitor.md, intercloud9-admin.md, intercloud9-dispositions.md, intercloud9-data-entities.md, intercloud9-vs-mightycall.md

**Key observations:**
- Single-pane agent workspace `Contact View` combines contact form + dialer + Disposition Bar + Read Script + Contact Log — different from MightyCall's split between List View and agent screen
- Top nav has 7 items: Home, List View, Contact View, Settings, Admin, Campaigns, Agent Monitor
- Per-user `Connect via` choice: SIP Phone (Username/Password) OR Telephone Dial-in (Agent ID/PIN) — admin-configurable in Admin → Users
- Read Script modal renders merge tags as coloured pills (e.g. `[Joey Cleint]`) — pulled from Contact fields; `Popup script on connect` checkbox auto-shows it
- Disposition Bar is two-level: 5 buckets (Custom, Schedule Callback, Made Contact, Unable to Contact, Assign to) with sub-dropdowns each
- Campaign-level `Dial Rate Override` dropdown: Auto / Inbound / 1 / 2 / 3 / 4 / 5 (lines per agent)
- Agent Monitor barge requires SIP connection; DTMF coaching codes: `2` whisper, `1` takeover, `3` conference
- Upload Contact has 4 dedupe/compliance checkboxes: Random / Prevent Dup in File (default ON) / Prevent Dup in Campaign (default ON) / Scrub Against DNC List (default ON) / **I am Allowed to Call These Contacts** (TCPA gate, default OFF — must be checked to upload)
- Graph Stats has two tabs: Disposition Data (agent-applied) and Calling Data (system: No Agent Available / Not Dispositioned / Carrier Error NTF)
- Export Contacts modal supports CDRs OR filtered Contacts List, async-emailed
- Recordings split: per-call (Contact View), per-agent (Admin row icon — "Direct Calls Only" tooltip), per-campaign (Campaigns row Website/CSV link)
- Lead ID field on Contact has greyed text "Change or add fields" → Admin → Setup Database Fields makes contact schema configurable
- Footer branding: `Copyright (c) 2008-16` — older product / 2016-era UI; bootstrap-style theming

**Discarded scenes:**
- Frames 0001-0013: intro / title — no UI
- Frames 0086-0102: transitions / talking-head between agent workspace shots
- Frames 0251-0263: talking head with no UI focus
- Frames 0273-0280: outro / closing

**Index updated:** Added "InterCloud9 Predictive Dialer Pages" section to index.md and added the demo to the Sources table

---

## 2026-04-19: EspoCRM Sales Pack deep-dive wiki added

**Source ingested:**
- `espocrm-sales/knowledge_graph.json` — EspoCRM Sales Pack tutorial (7:14, 9 significant scenes of 26 total, from 380 captured frames at 6m20s)

**Pages created:** 2
- espocrm-sales-pack.md, espocrm-sales-entities.md

**Key observations:**
- Full Sales & Purchases nav revealed: Products, Quotes, Sales Orders, Invoices, Delivery Orders, Return Orders, Purchase Orders, Receipt Orders, Transfer Orders, Inventory Adjustments, Warehouses, Inventory Numbers, Inventory Transactions
- Product has 3 tabs: Overview (qty breakdown), Price, Details (Is Inventory, Inventory Number Type, Removal Strategy FIFO)
- Inventory tracked per warehouse — Available = On Hand − Reserved; also Soft-Reserved, In Transit, On Order
- Serial number tracking: Is Inventory ✓ + Inventory Number Type = Serial → creates individual InventoryNumber records (e.g. ET-AA004)
- Warehouses: Main Warehouse, Repair Center, Store shown; each has Products panel + Inventory Numbers panel
- Purchase Orders (PO-NNNNN): "Create Receipt" button generates Receipt Order on delivery; Receipt Fully Created checkbox
- Transfer Orders (TO-NNNNN): inter-warehouse stock moves (e.g. Main → Repair Center); line items have Qty + Qty Rcv + Inventory Number
- Quote status "Approved" observed — extends prior wiki which only had Draft/Sent/Accepted/Rejected/Cancelled
- Quote actions: Print to PDF, Send in Email, Lock, Convert Currency, View Audit Log, View User Access
- Quote form: Account auto-populates Billing Address; "Copy Billing" button copies to Shipping Address
- Currency: Euro (€) throughout demo

**Discarded scenes:**
- Frames 0001-0042: our own terminal (capture setup)
- Frames 0253-0265: presenter talking head, no UI
- Frames 0377-0380: presenter outro

**Index updated:** Added "EspoCRM Sales Pack Pages" section to index.md

---

## 2026-04-16: EspoCRM Advanced wiki added

**Source ingested:**
- `espocrm/knowledge_graph.json` — EspoCRM Advanced tutorial (17:00, 19 significant scenes of 37 total, from 1020 captured frames)

**Pages created:** 8
- espocrm-modules.md, espocrm-enquiries.md, espocrm-contacts-accounts.md, espocrm-opportunities.md, espocrm-sales.md, espocrm-dashboard-reports.md, espocrm-workflows.md, espocrm-administration.md, espocrm-data-entities.md

**Key observations:**
- EspoCRM calls Leads "Enquiries" — URL uses /Lead/ internally but UI displays "Enquiries"
- Enquiry status pipeline: New → Assigned → In Process → Recycled → Dead (different from Salesforce)
- Opportunity stages: Prospecting → Qualification → Perception Analysis → Proposal/Price Quote → Negotiation/Review → Closed Won / Closed Lost
- Account types: Prospect, Customer, Investor, Partner, Reseller, Consultant
- Sales Pack extends core with Quotes (Q-NNNNN auto-numbering), Invoices, Sales Orders, Products, Purchase Orders, Inventory Management
- Advanced Pack adds Reports (Grid with drill-down), Workflows (condition→action), BPM
- Workflow example 1: Account created → Send Email welcome
- Workflow example 2: Opportunity reaches Proposal/Price Quote → Auto-create linked Quote
- Dashboards are per-user/role configurable — Sales Manager tab has 7 chart/table widgets
- Dashboard drill-down: click pie segment → modal with filtered record list
- Admin customisation: Entity Manager, Layout Manager, Label Manager — EspoCRM is highly customisable without code
- One very long scene (scene_07, 456s, 2:25–10:00) covered Lead conversion form + Contact/Account/Opportunity detail pages + Quote entity

**Discarded scenes:**
- Frames 0001-0039: Intro / presenter talking head over dashboard
- Frames 0144-0199: Loading states and transitions
- Various short scenes (< 5s): UI animation frames between navigation clicks
- Final frames 1016-1020: Outro

**Index updated:** Added EspoCRM section with 9 pages to index.md

---

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
