# Campaign Management

The core workflow of MightyCall's Auto Dialer module. Campaigns are outbound calling efforts configured through a 4-step wizard.

## Navigation

Auto Dialer (top nav) > Campaigns (dropdown) > Campaigns list

## Campaign Creation Wizard

| Step | Name | Purpose | Details |
|------|------|---------|---------|
| 1 | [General Settings](general-settings.md) | Basic campaign config | Name, description, timezone, dates, business hours, numbers, local presence |
| 2 | [Dialer Settings](dialer-settings.md) | Mode and timing | Choose dialing mode, configure mode-specific parameters, dispositions |
| 3 | [Agent Management](agent-management.md) | Staff assignment | Select agents for the campaign |
| 4 | [Record Lists](record-lists.md) | Contact data | Upload CSV, select existing lists, check coverage score |

## Campaigns List View

Columns displayed:
- **Status indicator** (colored icon + label)
- **NAME** — campaign name
- **DESCRIPTION** — campaign description text
- **AGENTS** — avatars of assigned agents
- **RECORDS** — CSV filename + record count
- **COVERAGE SCORE** — fraction (e.g., "2 of 3") + percentage (e.g., "66.67%")

Action controls per campaign:
- Play / Pause / Stop buttons (left side)
- Three-dot menu: Edit, Delete

## Campaign Statuses

See [Campaign Statuses](campaign-statuses.md) for full details.

| Status | Meaning |
|--------|---------|
| Preparing | Business number, agent, or record list not yet assigned |
| Scheduled | Set to start at a future date |
| Ready | Fully configured, ready to launch |
| Running | Currently active |
| Paused | Temporarily stopped |
| Completed | Finished |
| Incomplete | Missing required configuration |

## Edit Rules

- **Completed** campaigns cannot be edited
- **Running & Paused** campaigns allow limited edits only:
  - General settings: editable
  - Dialer settings: limited changes for Progressive and Predictive modes
  - Agent list: editable
  - Record list: not changeable while running
- **Running** campaigns cannot be deleted
- To edit: three-dot menu > Edit
- To delete: three-dot menu > Delete (not available for Running)

## DNC Integration

The campaigns list view shows the [DNC Compliance](dnc-compliance.md) panel in the top-right:
- National DNC list scrubber toggle
- Local DNC List with number count
