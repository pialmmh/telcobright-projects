# Salesforce Activities — Tasks, Events, Chatter

Activities include Tasks, Events, logged calls, and emails. All appear in the Activity panel on any record.

**Source**: `salesforce-crm/knowledge_graph.json` (scenes 263–276)

## Tasks

### List View (Tasks tab)
**Columns**: Subject, Name, Related To, Due Date, Status, Priority, Assigned Alias, Last Modified Date

**Action**: New Task button

### Create Form (New Task)
| Field | Type | Notes |
|-------|------|-------|
| Assigned To | Lookup | Default: current user |
| Related To | Lookup | Any record (Account, Contact, etc.) |
| Subject | Text | Required (e.g. "Call Paul") |
| Comments | Long text | |
| Due Date | Date | |
| Reminder Set | Checkbox | Enables date/time picker |
| Reminder Date | Date | |
| Reminder Time | Time | e.g. 12:00 |
| Status | Dropdown | Required: Not Started, In Progress, Completed |
| Name | Lookup | Contact or Lead |

### Task Status Values
Not Started → In Progress → Completed

Tasks can be marked **Completed** inline in the list view (click status cell). Completed tasks appear in the related record's Activity panel ("I had a task with [User]").

## Events

### Create Form (New Event)
Accessed from Calendar tab or "New Event" in Activity panel.

| Field | Type | Notes |
|-------|------|-------|
| Subject | Text | Required |
| All-Day Event | Checkbox | Hides time fields |
| Private | Checkbox | Visible only to admin and View All users |
| Start Date | Date | |
| Start Time | Time | |
| End Date | Date | |
| End Time | Time | |
| Location | Text | e.g. "Zoom" |
| Show Time As | Dropdown | Busy, Free |
| Description | Long text | |

Events appear on Calendar with a popup showing Location, Start/End, Edit, Delete.

## Calendar Views

| View | Description |
|------|-------------|
| Month | Full month grid (default) |
| Week | 7-day column layout |
| Day | Single day timeline |
| Table | List format |
| Availability | Team availability overlay |

**Right sidebar**: Mini calendar navigator, My Calendars section, Other Calendars section.

## Activity Panel (on all records)

Right sidebar present on: Leads, Accounts, Contacts, Opportunities, Cases, Campaigns.

### Tabs
- **Activity**: Feed of all activity actions
- **Chatter**: Social collaboration posts

### Quick Actions
- **Log a Call**: Add a call recap note
- **Email**: Send email from the record
- **New Task**: Create linked task
- **New Event**: Create linked event

### Activity Feed
- Shows **Upcoming & Overdue** tasks/events
- Shows past activities with timestamps
- Filters: All time | All activities | All types
- Expand All / View All links

## Chatter

Social collaboration on records.

### Actions
- Post (text, file, link)
- Comment on posts
- @mention users

Posts appear in the record's Chatter tab and in the global Chatter feed.

## See Also
- [salesforce-modules.md](salesforce-modules.md) — Activity panel on all records
