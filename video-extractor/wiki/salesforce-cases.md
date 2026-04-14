# Salesforce Cases

Cases are customer support tickets. Each case is linked to a Contact and Account, and tracked through a status pipeline.

**Source**: `salesforce-crm/knowledge_graph.json` (scenes 182–194)

## List View

**Columns**: Case Number, Case Status, Case Origin, Contact Name, Subject, Priority, Date/Time Opened, Owner Name

**Actions**: New, Change Owner, Update Case

Filterable by Priority and Case Origin.

### Case Origins
Facebook, Twitter, Email, Web, Phone

### Priority Levels
Critical, High, Medium, Low

## Status Pipeline

```
New → Open → Pending → Escalated → Closed
```

Shown as horizontal progress bar on Case detail. "Mark Status as Complete" button advances the case. Toast notification appears on status change.

## Create Form (New Case)

### Case Information
| Field | Type | Notes |
|-------|------|-------|
| Case Owner | Lookup | Assigned user |
| Case Number | Auto | System-generated |
| Contact Name | Lookup | Search with name autocomplete |
| Account Name | Auto-filled | From Contact |
| Web Email | Email | |

### Additional Information
| Field | Type | Options |
|-------|------|---------|
| Status | Dropdown | New, Open, Pending, Escalated, Closed |
| Type | Dropdown | Problem, Question, Feature Request |
| Case Origin | Dropdown | Facebook, Twitter, Email, Web, Phone |
| Case Reason | Dropdown | New problem, Instructions not clear, User didn't attend training |
| Priority | Dropdown | Critical, High, Medium, Low |

### Description Information
| Field | Type |
|-------|------|
| Subject | Text (required) |
| Description | Long text |
| Internal Comments | Long text (not visible to customer) |

## Case Detail Layout

Three-panel layout:

### Left Panel
- **Case Details**: Case Number, Case Owner, Status, Priority, Subject, Description
- **Contact Details**: Name, Title, Account Name, Phone, Email (all clickable links)
- **Cases for Parent Contact**: Related cases from same contact

### Center
- **Feed tab**: Email, Log a Call, Post, Status Changes timeline
- **Details tab**: All case fields in edit mode

### Right Panel
- **Knowledge tab**: Search Knowledge (keyword search), Suggested Articles
- **Related tab**: Related records

## Knowledge Base

Sidebar on Case detail. When viewing a case, agents can:
1. Search internal knowledge articles by keyword
2. See auto-suggested articles based on case subject
3. Attach articles to the case response

## See Also
- [salesforce-modules.md](salesforce-modules.md) — Cross-module features
- [salesforce-data-entities.md](salesforce-data-entities.md) — Case entity fields
