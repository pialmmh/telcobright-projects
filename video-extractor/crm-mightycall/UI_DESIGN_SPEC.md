# MightyCall Predictive Dialer UI Design Specification

## Layout & Patterns

**Layout Type**: Top navigation bar with dropdown sub-menus. Wizard/stepper for campaign creation (4 steps in left sidebar). Two-column layout on creation forms (settings left, supporting panel right).
**Color Scheme**: Dark navy/black top nav. White content area. Green accent (#00CC00 lime) for active nav items and brand elements. Blue action buttons. Status badges with color coding (green=Running, yellow=Ready/Incomplete, grey=Completed, orange=Paused).
**Component Library**: Custom design system. Uses card panels, toggle switches, data tables with sortable columns, step-wizard sidebar, date pickers, AM/PM time inputs.

### Common Patterns

- 4-step campaign creation wizard with left sidebar progress tracker
- Right-side resource panel (numbers, record lists) alongside main form
- Toggle switches for enable/disable features
- Inline status badges on list screens
- Disposition tables with Retry/Final radio selectors and retry period inputs
- Coverage score metric linking local numbers to contact area codes
- Agent availability status indicator top-right (green dot + Available + timer)

## Screen Specifications

### Campaigns List

**URL Pattern**: `/auto-dialer/campaigns`

**Components**:
| Type | Label | Action |
|------|-------|--------|
| button | Create campaign | Opens campaign creation wizard |
| table | Campaigns table | Lists all campaigns with Name, Description, Agents, Records, Coverage Score columns |
| badge | Status badge | Shows Running / Ready / Completed / Paused / Incomplete per campaign |
| button | Play/Pause | Start or pause a campaign inline |
| panel | National DNC list scrubber | Upload DNC compliance list |
| button | Upload (DNC) | Upload DNC CSV file |
| link | Download template | Download DNC CSV template |

---

### Campaign General Settings (Step 1)

**URL Pattern**: `/auto-dialer/campaigns/create/general`

**Components**:
| Type | Label | Action |
|------|-------|--------|
| input | Campaign name | Enter campaign title |
| textarea | Description (Optional) | Enter campaign description, 200 char limit |
| dropdown | Timezone | Select campaign timezone (e.g. UTC-06:00 Central Time) |
| date_picker | Start date | Set campaign start date (optional) |
| date_picker | End date | Set campaign end date (optional) |
| schedule_grid | Business hours | Enable/disable each day and set AM/PM start-end times or Full Day |
| panel | Business Numbers | Assign phone numbers to the campaign with labels (LA Main, LA Sales, NYC, Toronto, San Diego, Toll-Free) |
| toggle | Auto-rotation | Enable number rotation |
| toggle | Local Presence | Auto-select best number based on contact area code |
| button | Cancel | Discard campaign and return to list |
| button | Save | Save campaign progress |

---

### Campaign Dialer Settings (Step 2)

**URL Pattern**: `/auto-dialer/campaigns/create/dialer`

**Components**:
| Type | Label | Action |
|------|-------|--------|
| radio_group | Dialer mode selector | Choose Preview / Progressive / Predictive / Agentless |
| toggle | Auto answer | Enable automatic call pickup by agents |
| number_input | Timeout (sec) | Seconds before auto-answer triggers |
| number_input | Ringing agent time (sec) | How long agent phone rings |
| number_input | Wrap-up time (sec) | Post-call wrap time before next call |
| number_input | Max ring time (sec) | Maximum time to let contact phone ring |
| number_input | Default retry period (min) | Minimum wait before retrying a record |
| number_input | Max attempts per record | Maximum total dial attempts per contact |
| dropdown | Calls per agent | Set simultaneous calls per agent (Auto or manual) |
| number_input | Abandon rate (%) | Maximum acceptable abandoned call percentage |
| toggle | Answering machine detection | Enable AMD |
| disposition_table | System disposition | Set Retry/Final rules for system-level outcomes (busy, no response, AMD, invalid, blocked) |
| disposition_table | Agent disposition | Configure which outcome options agents can select and whether each is Final |

---

### Campaign Record List (Step 4)

**URL Pattern**: `/auto-dialer/campaigns/create/records`

**Components**:
| Type | Label | Action |
|------|-------|--------|
| dropzone | Create record list | Upload or drag-and-drop CSV file |
| button | Upload | Trigger file upload |
| link | Download the template | Download CSV template with required field format |
| list | Existing record lists panel | Browse and select pre-uploaded lists showing record count and unique area codes |
| radio | New record list | Create a new list rather than reusing existing |
| column | Coverage Score | Shows % of contact area codes covered by assigned local numbers |

---

### Reports - Campaigns

**URL Pattern**: `/reports/campaigns`

**Components**:
| Type | Label | Action |
|------|-------|--------|
| date_filter | Date range filter | Filter report by date range with preset options (last 30 days, etc.) |
| tabs | Report tabs | Switch between Campaigns / Dispositions / Agent sessions / Call details |
| table | Campaign metrics table | Shows all campaigns with KPI columns |
| button | Columns | Show/hide specific metric columns |
| button | Export | Export report data |

---

