# InterCloud9 — Campaigns

Where admins/supervisors create campaigns, upload contact lists, configure dial behaviour, and monitor real-time stats. URL: `/#/campaign`.

**Source**: `intercloud9-dialer/knowledge_graph.json` (frames 0142, 0160, 0189, 0204, 0217)
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Campaigns list

```
┌────────────────────────────────────────────────────────────────────┐
│ Current Campaigns  [+ Create New Campaign]      3 Total Campaigns │
├────────────────────────────────────────────────────────────────────┤
│ Business ●               [actions]   Total Contacts: 691          │
│ +1 (212) 555-1212 / Your Name        Connected:       8           │
│                                      Unanswered:      4           │
│ ┌───┬───┐                            Remaining:  679 (677 avail.) │
│ │ ✏ │ ⟳ │                            Abandon Rate: 0.000% [Reset] │
│ ├───┼───┤                            Recordings: Website / CSV    │
│ │ 🗑 │ + │                            API:        Import           │ ◯ pie
│ ├───┼───┤                                                          │
│ │ 🔊│ 🌿│                                                          │
│ ├───┼───┤  Legend: 677 Uncalled · 2 Out of Time · 12 Called Once  │
│ │ ⬆ │ 📊│                                                          │
│ └───┴───┘                                                          │
├────────────────────────────────────────────────────────────────────┤
│ Consumer ●                                                         │
│ Test ●                                                             │
└────────────────────────────────────────────────────────────────────┘
```

### Per-campaign action toolbar

8 icons in a 4 × 2 grid to the left of the metrics:

| Icon | Action |
|------|--------|
| ✏️ pencil (orange) | Edit campaign — opens the *Edit Predictive Campaign* modal |
| ⟳ refresh (blue) | Refresh stats |
| 🗑 trash (red) | Delete campaign |
| ➕ plus (blue) | Add new contact (opens Upload Contact for this campaign) |
| 🔊 speaker (blue) | Audio / IVR / Play Msg upload |
| 🌿 leaf (green) | Toggle active / running state |
| ⬆ upload | Export contacts |
| 📊 stats (blue) | Open Graph Stats modal |

### Per-campaign metrics

| Metric | Notes |
|--------|-------|
| Total Contacts | All uploaded |
| Connected Contacts | Reached a live person |
| Unanswered Contacts | Rang out / no answer |
| Remaining Contacts | `X (Y available)` — Y is what's actually callable now after DNC + time-of-day + dispositions |
| Abandon Rate | Percent + **Reset** link |
| Recordings | **Website** / **CSV** download links |
| API | **Import** link (programmatic upload) |
| Pie chart | Three slices: green Uncalled, red Out of Time, grey Called Once |

## Edit Predictive Campaign modal

Triggered by the ✏️ icon.

| Field | Type | Notes |
|-------|------|-------|
| Name | text | required |
| Description | text | optional |
| Caller ID Name | text | required — what the call recipient sees |
| Caller ID Number | phone | required, validated `Must Be A Valid Phone Number` |
| Limit Calling Hours | checkbox | enables the two time fields below |
| Never Call Before | time dropdown | e.g. `8:00 (8:00 am)` |
| Never Call After | time dropdown | e.g. `17:00 (5:00 pm)` |
| Dial Rate Override | dropdown | `Auto · Inbound · 1 · 2 · 3 · 4 · 5` (lines per agent) |
| Wait for Agent | checkbox | wait for an idle agent before dialing |

Action: **Save Campaign** (orange) / **Cancel** (blue).

### Dial Rate Override values explained

| Value | Behaviour |
|-------|-----------|
| Auto | System computes optimal lines based on abandon-rate target |
| Inbound | Campaign accepts inbound only (no outbound dial) |
| 1–5 | Fixed lines-per-agent ratio (5 = aggressive predictive) |

## Upload Contact modal

Triggered by the ➕ icon. Three numbered steps shown in the modal header:

1. Select a CSV file by pressing **Load CSV File**
2. Select the appropriate field for any columns
3. When complete, press **Upload**

### CSV column mapper

Each column from the uploaded CSV gets a dropdown to pick which Contact field it maps to. Available targets (seen in the dropdown):

`Phone (required *)` · First Name · Last Name · Address · City · Company · State · Zip · Other · Email · Lead ID

The right side of the modal shows live preview rows from the CSV so the admin can confirm the mapping is correct.

### Options checkboxes

| Option | Default | Notes |
|--------|---------|-------|
| Random | off | Randomise dial order |
| Prevent Duplicate Phone Number in File | ON | Dedupe within the upload |
| Prevent Duplicate Phone Number in Campaign | ON | Dedupe against existing campaign contacts |
| Scrub Against our Do-Not-Call List | ON | National DNC scrub |
| **I am Allowed to Call These Contacts** | OFF | **TCPA gate** — must be checked before Upload enables |

Action: **Upload** (orange) / **Cancel** (blue).

## Graph Stats modal

Triggered by the 📊 icon. Two tabs:

### Disposition Data tab
Pie chart of agent-applied dispositions for the campaign.

### Calling Data tab
System-side outcomes:
- **No Agent Available** (blue)
- **Not Dispositioned** (grey) — typically the largest slice (e.g. 80%)
- **Carrier Error NTF** (red) — *Number That Failed*

Hovering a pie segment shows a tooltip overlay with the percentage and label. Single **Cancel** button to close.

## Export Contacts modal

Email-export of either CDRs or filtered contact list.

### Export type (radio)
- **Call Detailed Records (CDRs)** — list of all calls made for this campaign
- **Contacts List** — list of all contacts, their disposition, and call statuses

### Disposition filter (only with Contacts List)
Checkbox list — `Check All | Uncheck All` shortcut at top:

`Direct Call · Inbox · Scheduled Callback · Sale/Goal/Lead · Not Interested/Dead · No Contact · Wrong Number · Machine Left Msg`

### Delivery
- **Send to Email** field (required) — async export, emailed when ready

Action: **Export** (orange) / **Cancel** (blue).

## See Also
- [intercloud9-dispositions.md](intercloud9-dispositions.md) — disposition catalogue used in Graph Stats and Export
- [intercloud9-data-entities.md](intercloud9-data-entities.md) — Campaign, Contact, CallRecord schemas
- [intercloud9-contact-view.md](intercloud9-contact-view.md) — where uploaded contacts get worked
