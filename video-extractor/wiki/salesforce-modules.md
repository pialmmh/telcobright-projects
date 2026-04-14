# Salesforce Sales Cloud — Module Overview

Core modules visible in top navigation. All share cross-module features: Activity panel, Chatter, list view controls, toast notifications, duplicate detection.

**Source**: `salesforce-crm/knowledge_graph.json`

## Navigation

```
Home | Leads | Accounts | Contacts | Opportunities | Cases | Tasks | Calendar | Reports | Dashboards | Campaigns
```

Global search bar (top center), user avatar + settings (top right).

## Module Summary

| Module | Purpose | Key List Columns |
|--------|---------|-----------------|
| **Home** | Landing dashboard | Pipeline chart, Tasks, Recent records, Assistant |
| **Leads** | Unqualified prospects | Name, Company, Lead Status, Phone, Email, Owner |
| **Accounts** | Companies/businesses | Account Name, Billing State, Phone, Type |
| **Contacts** | Individuals at Accounts | Name, Account Name, Phone, Email |
| **Opportunities** | Active deals | Opportunity Name, Account, Stage, Close Date, Amount |
| **Cases** | Support tickets | Case #, Status, Origin, Priority, Subject |
| **Tasks** | To-do items | Subject, Name, Related To, Due Date, Status, Priority |
| **Calendar** | Events and scheduling | Month/Week/Day/Table/Availability views |
| **Reports** | Saved data analysis | Report Name, Folder, Type |
| **Dashboards** | Visual KPI boards | Dashboard Name, Folder |
| **Campaigns** | Marketing campaigns | Campaign Name, Type, Status, Start/End Date, Responses |

## Cross-Module Features

### Activity Panel (right sidebar on all records)
- Tabs: Activity | Chatter
- Actions: Log a Call, Email, New Task, New Event
- Sections: Upcoming & Overdue, Past Activities
- Filters: All time / All activities / All types

### List View Controls (on all list views)
- **Modes**: Table, Kanban (where applicable), Split-pane (list + detail side by side)
- **Actions**: New, Import, Printable View, Search, Filter, Edit columns, Column sort
- **Pinning**: Any list view can be pinned as default
- **Inline editing**: Update fields directly in table row
- **Search note**: Date/reference/count fields not keyword-searchable — use column filters instead

### Common UI Patterns
- **Record header**: Breadcrumb + record name + quick stats + action buttons
- **Status pipeline bar**: Horizontal progress bar with clickable stage steps (Leads, Opportunities, Cases)
- **Modal create forms**: Overlay with sectioned fields, Save / Save & New / Cancel
- **Toast notifications**: Green success banners ("Record was created", "Status changed")
- **Duplicate detection**: "We found no potential duplicates" banner on new records
- **Collapsible sections**: Details, Address Information, Additional Information, System Information

## See Also
- [salesforce-leads.md](salesforce-leads.md) — Lead lifecycle and conversion
- [salesforce-opportunities.md](salesforce-opportunities.md) — Deal stages and pipeline
- [salesforce-cases.md](salesforce-cases.md) — Case management and knowledge
- [salesforce-activities.md](salesforce-activities.md) — Tasks, Events, Chatter
- [salesforce-campaigns.md](salesforce-campaigns.md) — Campaign and ROI tracking
- [salesforce-reports.md](salesforce-reports.md) — Reports and Dashboards
- [salesforce-data-entities.md](salesforce-data-entities.md) — All fields and relationships
