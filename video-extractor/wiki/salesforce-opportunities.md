# Salesforce Opportunities

Opportunities are deals in progress. Each has a **Stage** with an associated **Probability (%)** that advances through a pipeline.

**Source**: `salesforce-crm/knowledge_graph.json` (scenes 158–174)

## List View

**Columns**: Opportunity Name, Account Name, Owner Full Name, Amount, Close Date, Stage, Probability (%), Follow Up?

**Actions**: New, Mass Update, Printable View

**Modes**: Table | Kanban | Split-pane

### Kanban / Pipeline View
Columns by Stage with card count and total £ amount:

```
Qualification (2, £68,000) | Example Stage (0) | Proposal/Price Quote (1, £19,800)
| Negotiation/Review (2, £75,550) | Closed Won (5, £187,350)
```

Cards show: Opportunity name, Amount, Account, Owner.

### Split-Pane View
List on left, record detail on right — fast navigation without full page reload.

## Stage Pipeline & Probability

| Stage | Probability |
|-------|------------|
| Qualification | 20% |
| Proposal/Price Quote | 65% |
| Negotiation/Review | 75% |
| Closed Won | 100% |
| Closed Lost | 0% |

Progress bar is shown on Opportunity detail. Indicator shows "X days in [Stage]".

## Closing an Opportunity

Click **"Select Closed Stage"** button (or move to Closed column in Kanban). A **"Close This Opportunity"** modal appears with:

```
Stage dropdown:
  - Select a closed stage...
  - Closed Won
  - Closed Lost
```

## Create / Edit Form

| Field | Type | Notes |
|-------|------|-------|
| Opportunity Name | Text | Required |
| Account Name | Lookup | Link to Account |
| Close Date | Date | Required |
| Stage | Dropdown | Required |
| Amount | Currency | |
| Type | Dropdown | New Business, Existing Business |
| Lead Source | Dropdown | Trade Show, Web, etc. |
| Next Step | Text | |
| Description | Long text | |
| Follow Up? | Checkbox | |
| Probability (%) | Number | Auto-set by Stage, editable |

## Opportunity Detail Page

- **Header**: Account Name, Close Date, Amount, Opportunity Owner
- **Stage bar**: Clickable pipeline steps, "Mark Stage as Complete" button
- **Tabs**: Details, Contacts, Cases, Notes & Files
- **Activity tabs**: Activity | Chatter | Stage History
- **Header actions**: Follow, Edit, Update Next Steps, Change Owner

## Linking to Campaigns

Opportunities can be linked to a Campaign via the **Primary Campaign Source** field (also set on Lead via Lead Source field). This allows Campaign ROI tracking.

## See Also
- [salesforce-leads.md](salesforce-leads.md) — Lead conversion creates Opportunities
- [salesforce-campaigns.md](salesforce-campaigns.md) — Campaign ROI via Opportunity linking
- [salesforce-data-entities.md](salesforce-data-entities.md) — Opportunity entity fields
