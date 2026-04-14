# Salesforce Campaigns

Campaigns track marketing efforts and their ROI by linking Leads, Contacts, and Opportunities.

**Source**: `salesforce-crm/knowledge_graph.json` (scenes 293–352)

## List View

**Columns**: Campaign Name, Parent Campaign, Type, Status, Start Date, End Date, Responses in Campaign, Owner Alias

**Actions**: New, Printable View

### Saved List Views
- **Recently Viewed** (default)
- **All Active Campaigns** (filtered by Active=true, pinnable)
- Custom views can be created and pinned

**Search note**: Parent Campaign, Start Date, End Date, Responses, and Owner Alias are not keyword-searchable — use column filters instead.

## Create Form (New Campaign)

### Basic Information
| Field | Type | Notes |
|-------|------|-------|
| Campaign Owner | Lookup | Default: current user |
| Status | Dropdown | Planned, Active, Aborted, Completed |
| Campaign Name | Text | Required |
| Active | Checkbox | Controls "All Active Campaigns" filter |
| Type | Dropdown | Referral Program, Email, Webinar, Conference, Direct Mail, Advertisement |
| Parent Campaign | Lookup | Hierarchical campaigns |
| Description | Long text | |

### Planning Section
| Field | Type |
|-------|------|
| Start Date | Date |
| End Date | Date |
| Num Sent in Campaign | Number |
| Expected Response (%) | Percentage |
| Expected Revenue in Campaign | Currency |
| Budgeted Cost in Campaign | Currency |
| Actual Cost in Campaign | Currency |

## Campaign Detail Page

### Header
Type, Status, Start Date, End Date displayed below campaign name.

**Action buttons**: New Contact, New Opportunity, New Case

### Related Tab
- **Opportunities (0)**: Opportunities linked via Primary Campaign Source
- **Attachments**: Upload files or drag-and-drop
- **Campaign Members**: Add Leads, Add Contacts buttons

### Activity Panel
New Event, New Task, Log a Call, Email actions.

## Campaign ROI Tracking

Opportunities link to campaigns via the **Primary Campaign Source** field on the Opportunity (populated from the Lead's Lead Source when converting a lead from a campaign member).

Campaign detail → Opportunities tab shows all deals attributed to the campaign.

## Campaign Statuses

| Status | Meaning |
|--------|---------|
| Planned | Created, not yet launched |
| Active | Currently running |
| Aborted | Cancelled mid-run |
| Completed | Finished |

## Campaign Types

Referral Program, Email, Webinar, Conference, Direct Mail, Advertisement

## See Also
- [salesforce-opportunities.md](salesforce-opportunities.md) — Opportunity → Campaign linking
- [salesforce-leads.md](salesforce-leads.md) — Leads as Campaign Members
- [salesforce-data-entities.md](salesforce-data-entities.md) — Campaign entity fields
