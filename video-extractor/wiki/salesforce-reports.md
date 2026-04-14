# Salesforce Reports & Dashboards

Reports provide data analysis; Dashboards are visual KPI boards composed of report widgets.

**Source**: `salesforce-crm/knowledge_graph.json` (scenes 277–292)

## Reports

### Report List

**Columns**: Report Name, Description, Folder, Created By, Created On, Subscribed

**Actions**: New Report, New Report (Salesforce Classic), Search reports

### Left Sidebar Navigation

```
REPORTS
  Recent
  Created by Me
  Private Reports
  Public Reports
  All Reports

FOLDERS
  All Folders
  Created by Me
  Shared with Me

FAVORITES
  All Favorites
```

### Report Types
- **Tabular**: Simple list of records
- **Summary**: Grouped rows with subtotals
- **Matrix**: Rows and columns with cross-totals
- **Joined**: Multiple report blocks

### Sample Reports Observed
| Report Name | Type | Grouping | Total |
|------------|------|---------|-------|
| Opportunity Pipeline | Matrix | Stage (rows) | £210,800 |
| HomePage - Potential Revenue Source | — | — | — |
| HomePage - All Pipeline - Current Year | — | — | — |

### Opportunity Pipeline Report (Matrix)
- Rows grouped by **Stage**
- Sub-rows with detail: Amount, Type, Lead Source, Close Date, Next Step, Probability (%), Fiscal Period, Age, Created Date, Account Name

## Dashboards

### Dashboard List

**Columns**: Dashboard Name, Description, Folder, Created By, Created On, Subscribed

**Actions**: New Dashboard, Search dashboards, Refresh, Edit, Subscribe

### Left Sidebar Navigation

```
DASHBOARDS
  Recent
  Created by Me
  Private Dashboards
  All Dashboards

FOLDERS
  All Folders
  Created by Me
  Shared with Me

FAVORITES
  All Favorites
```

### Sample Dashboard: "Sales Pipeline"

**Header KPI**: Opportunity Pipeline Set to Close This Quarter — **£210,800**

| Widget | Type | Dimension | Period |
|--------|------|-----------|--------|
| Leads Created | Donut chart | Lead Source | Current FY |
| Leads Converted to Opportunities | Donut chart | Lead Owner | Current FY |
| Total Pipeline by Stage | Table | Stage | Current FY |
| Leads Created - Monthly Trend | Bar chart | Month | — |
| Open Leads | Table | — | — |
| Open Pipeline by Owner | Table | Opportunity Owner | Current FY |

### Total Pipeline by Stage (from dashboard)
| Stage | Amount |
|-------|--------|
| Negotiation/Review | £75,550 |
| Qualification | £68,000 |
| Meeting Scheduled | £25,750 |
| Proposal/Price Quote | £19,500 |
| Example Stage | £10,000 |

## See Also
- [salesforce-opportunities.md](salesforce-opportunities.md) — Opportunity data feeding reports
- [salesforce-modules.md](salesforce-modules.md) — Module overview
