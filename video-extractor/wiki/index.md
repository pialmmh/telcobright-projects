# CRM Knowledge Wiki

Compiled from video tutorials covering MightyCall Auto Dialer, Salesforce Sales Cloud, and EspoCRM.

## Sources

| Video | Duration | Scenes | Focus |
|-------|----------|--------|-------|
| [Predictive Dialer](../crm-mightycall/knowledge_graph.json) | 8:00 | 15 | Predictive mode, campaign analytics, reports |
| [Preview Dialer](../preview-dialer/knowledge_graph.json) | 6:18 | 21 | Preview mode, agent workspace, DNC compliance |
| [Progressive Dialer](../progressive-dialer/knowledge_graph.json) | 6:52 | 19 | Progressive mode, AMD, auto-answer |
| [Salesforce Sales Cloud](../salesforce-crm/knowledge_graph.json) | ~40:00 | 81 | Full CRM: Leads, Accounts, Contacts, Opportunities, Cases, Tasks, Calendar, Reports, Dashboards, Campaigns |
| [EspoCRM Advanced](../espocrm/knowledge_graph.json) | 17:00 | 19 | CRM: Enquiries, Contacts, Accounts, Opportunities, Quotes, Dashboard, Reports, Workflows, Administration |

---

## MightyCall Auto Dialer Pages

### Core Concepts
- [Campaign Management](campaign-management.md) — Creating, editing, and managing outbound campaigns
- [Dialing Modes](dialing-modes.md) — Preview, Progressive, Predictive, and Agentless compared

### Features
- [General Settings](general-settings.md) — Step 1 of campaign wizard (name, timezone, hours, numbers)
- [Dialer Settings](dialer-settings.md) — Step 2: mode-specific timing, attempts, dispositions
- [Agent Management](agent-management.md) — Step 3: agent assignment and workspace
- [Record Lists](record-lists.md) — Step 4: CSV upload, coverage score, list management
- [Dispositions](dispositions.md) — System (auto) and Agent (manual) call outcomes
- [DNC Compliance](dnc-compliance.md) — National scrubber, local DNC list, TCPA compliance
- [Local Presence](local-presence.md) — Area code matching for higher answer rates

### Reference
- [Campaign Statuses](campaign-statuses.md) — Preparing, Scheduled, Running, Ready, Completed, Paused, Incomplete
- [Data Entities](data-entities.md) — Campaign, Dialer Settings, Record List, Disposition, Business Number
- [UI Patterns](ui-patterns.md) — Layout, navigation, component patterns

### Mock Screens (styling reference)
- [`../mock-screens/mightycall-campaigns.html`](../mock-screens/mightycall-campaigns.html) — Campaigns list view: sidebar, top nav, status badges, DNC panel, agent avatars, coverage score, action buttons. Use as CSS/layout baseline.

---

## Salesforce Sales Cloud Pages

### Overview
- [salesforce-modules.md](salesforce-modules.md) — All modules, navigation, cross-module features

### Modules
- [salesforce-leads.md](salesforce-leads.md) — Lead lifecycle, Kanban stages, Lead Conversion
- [salesforce-opportunities.md](salesforce-opportunities.md) — Deal pipeline, stages, probability, Kanban view
- [salesforce-cases.md](salesforce-cases.md) — Support tickets, tri-panel layout, Knowledge base
- [salesforce-activities.md](salesforce-activities.md) — Tasks, Events, Calendar, Chatter, Activity panel
- [salesforce-campaigns.md](salesforce-campaigns.md) — Campaign creation, members, ROI tracking
- [salesforce-reports.md](salesforce-reports.md) — Reports (matrix/summary) and Dashboards with widgets

### Reference
- [salesforce-data-entities.md](salesforce-data-entities.md) — All entity fields and relationships (Lead, Account, Contact, Opportunity, Case, Task, Event, Campaign, Report, Dashboard)

---

## EspoCRM Pages

### Overview
- [espocrm-modules.md](espocrm-modules.md) — All modules, navigation structure, cross-module features, UI layout patterns

### CRM Modules
- [espocrm-enquiries.md](espocrm-enquiries.md) — Enquiries (Leads): status pipeline New→Assigned→In Process→Recycled→Dead, conversion flow
- [espocrm-contacts-accounts.md](espocrm-contacts-accounts.md) — Contacts and Accounts entities, Account types
- [espocrm-opportunities.md](espocrm-opportunities.md) — Deal pipeline, 7 stages, line items, Quote automation

### Sales & Automation
- [espocrm-sales.md](espocrm-sales.md) — Quotes (Q-NNNNN), Invoices, Sales Orders, Products (Sales Pack)
- [espocrm-workflows.md](espocrm-workflows.md) — Workflow automation: conditions, Send Email, Create Record actions
- [espocrm-dashboard-reports.md](espocrm-dashboard-reports.md) — Dashboard tabs (My Items, Sales Manager), chart widgets, Grid reports with drill-down

### Administration
- [espocrm-administration.md](espocrm-administration.md) — Admin panel, customisation tools, extensions (Advanced Pack, Sales Pack, Project Management)

### Reference
- [espocrm-data-entities.md](espocrm-data-entities.md) — All entity fields and relationships (Enquiry, Contact, Account, Opportunity, Quote, Task, Report, Workflow)
