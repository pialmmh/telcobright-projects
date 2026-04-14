# Salesforce Leads

Leads are unqualified prospects. Once qualified, they are **converted** into an Account + Contact + Opportunity simultaneously.

**Source**: `salesforce-crm/knowledge_graph.json` (scenes 2–141)

## List View

**Columns**: Name, Company, State/Province, Phone, Email, Lead Status, Follow, Owner, Created Date

**Actions**: New, Import, Printable View, Search, Filter

**Modes**: Table | Kanban

### Kanban View
Leads grouped by status in draggable columns:

```
New (5) | Contacted (3) | Working (3) | Unqualified (0)
```

Cards show: Lead Name, Company, Location, Phone. Drag-and-drop to move between stages.

## Lead Status Pipeline

```
New → Working → Unqualified → Converted
```

Shown as horizontal progress bar on Lead detail page. Click any stage to move the lead.

## Create / Edit Form

### Basic Information
| Field | Type | Notes |
|-------|------|-------|
| Salutation | Dropdown | Mr., Ms., Dr., etc. |
| First Name | Text | |
| Last Name | Text | Required |
| Company | Text | Required |
| Title | Text | |
| Phone | Phone | |
| Mobile | Phone | |
| Email | Email | |
| Website | URL | |
| Lead Status | Dropdown | New, Working, Unqualified, Converted |
| Rating | Dropdown | Hot, Warm, Cold |
| Follow Up? | Checkbox | |

### Lead Source Options
Advertisement, Employee Referral, External Referral, In-Store, On Site, Other, Social, Trade Show, Web, Word of mouth

### Address Information
Address, City, State/Province, Postal Code, Country

### Additional Information
| Field | Type |
|-------|------|
| No. of Employees | Number |
| Annual Revenue | Currency |
| Industry | Dropdown |
| Description | Long text |

## Lead Detail Page

- **Header**: Follow, Edit, Convert, Change Owner buttons
- **Status bar**: New → Working → Unqualified → Converted (clickable stages)
- **Right panel**: Activity tab (Log a Call, Email, New Task, New Event) + Chatter tab
- **Duplicate detection banner**: "We found no potential duplicates of this Lead"

## Lead Conversion

Button: **Convert** (top right of Lead detail)

### Conversion Dialog
- Creates **Account + Contact + Opportunity** simultaneously
- Fields: Record Owner, Converted Status (e.g. "Qualified")
- Success modal shows names of created Account, Contact, and Opportunity

### What Conversion Does
```
Lead (Nick Boardman, CRMCrew)
  ├── Account created: CRMCrew
  ├── Contact created: Nick Boardman (Director)
  └── Opportunity created: CRMCrew-
```

## See Also
- [salesforce-opportunities.md](salesforce-opportunities.md) — Deals created from converted leads
- [salesforce-data-entities.md](salesforce-data-entities.md) — Lead entity fields
