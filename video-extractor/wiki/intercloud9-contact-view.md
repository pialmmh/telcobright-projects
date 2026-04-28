# InterCloud9 — Contact View (Agent Workspace)

The screen the agent stares at all day. Two-column layout: contact info on the left, call control + disposition + history on the right. URL pattern: `/#/contact/[contact_id]`.

**Source**: `intercloud9-dialer/knowledge_graph.json` (frames 0029, 0055, 0070, 0079, 0094, 0110, 0125)
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Layout

```
┌─────────────────────────┬───────────────────────────────────────────┐
│ Business: Unknown       │ Connection Status                       ●○│
│                         │ ✏️ 📋 ⓘ  [Manual Dial][Campaign Dial▾] +1 │
│ First Name: Joey        │                                           │
│ Last Name:  Cleint      │ 📞 ☎ ◀))) ⏺ ⏩ 👤 ✉ ◀ ▶                    │
│ Company:    interCloud9 │ Get  Hang Play Rec Trf 3-Way Email Prv Nx │
│ Address:    123 Happy   │                                           │
│ City:       Happy Vlle  │ Disposition Bar:                          │
│ State:      CA          │ □ Popup script on connect                 │
│ Zip:        123456      │ ☑ Upon disposition, load next call        │
│ Other:                  │ [Custom▾][Schedule Callback▾][Made Cont▾] │
│ Email:      joey@…      │ [Unable to Contact▾][Assign to▾]          │
│ Lead ID:    Change/add  │                                           │
│             fields      │ Contact Log: [Date][Message]              │
│                         │ ┌─────────┬──────────────────────────┐   │
│                         │ │ 16 Sep… │ Demo noted Leave a note  │   │
│                         │ │ 15 Sep… │ Demo noted Leave a note  │   │
│                         │ │ 15 Sep… │ [auto] assigned to Web…  │   │
│                         │ │ 15 Sep… │ Web Admin scheduled fol… │   │
│                         │ └─────────┴──────────────────────────┘   │
│                         │                                           │
│                         │ Add Note: [textarea] [Add Note]          │
└─────────────────────────┴───────────────────────────────────────────┘
```

## Contact form (left)

| Field | Type | Notes |
|-------|------|-------|
| Business | label | Block at very top, default *Unknown*. Provides context category for the contact. |
| First Name | text | |
| Last Name | text | |
| Company | text | |
| Address | text | |
| City | text | |
| State | text | |
| Zip | text | |
| Other | text | Free-form custom field |
| Email | email | |
| Lead ID | text | External lead-system reference. The greyed text *"Change or add fields"* on Lead ID indicates the field set is configurable via Admin → Setup Database Fields. |

## Connection Status panel (right)

### Header bar
- ✏️ edit, 📋 notes, ⓘ info icons
- **Manual Dial** button (orange highlight when active)
- **Campaign Dial ▾** / **Direct Dial ▾** dropdown — switches dialer source
- Live phone number display (e.g. `+1 (877) 256-2100`)

### Action button row
| Icon | Label | Action |
|------|-------|--------|
| 📞 (green) | Get Contact | Pull next contact from the active campaign queue |
| ☎ (orange) | Hangup | End current call |
| 🔊 | Play Msg | Play a pre-recorded voicemail / message |
| ⏺ | Record | Start manual recording (also drives the Recordings link) |
| ⏩ | Transfer | Send call to another agent (closer/specialist) |
| 👤 | 3-Way | Three-way conference |
| ✉ | Send Email | Email the current contact |
| ◀ | Previous | Navigate to previous contact in queue |
| ▶ | Next | Navigate to next contact |

### Disposition Bar
Two checkboxes inline with the bar:
- **Popup script on connect** — auto-opens the Read Script modal when the call connects.
- **Upon disposition, load next call** (default ON) — auto-advances to next contact after disposition.

Five dropdowns, each with sub-menu options:

| Bucket | Examples |
|--------|----------|
| Custom ▾ | User-defined custom dispositions |
| Schedule Callback ▾ | Opens the Schedule Follow-up modal |
| Made Contact ▾ | Sale/Goal/Lead, Inbox, Direct Call |
| Unable to Contact ▾ | No Contact, Wrong Number, Machine Left Msg, Not Interested/Dead |
| Assign to ▾ | Reassign ownership to another agent (closer/specialist) |

See [intercloud9-dispositions.md](intercloud9-dispositions.md) for the full catalogue.

### Contact Log
Tabular call/note history. Columns: **Date**, **Message**.

System-generated entries are bracketed with `[auto]`, e.g.:
```
[auto] assigned contact to Web Admin
Web Admin scheduled a follow-up call on Fri, 30 Sep at 08:00AM PDT
```

### Add Note
Free-text textarea + **Add Note** button. New notes appear at the top of Contact Log.

## Modals reachable from this screen

### Read Script modal
Opens manually (📋 icon) or automatically when the call connects (if *Popup script on connect* is checked).

Body is a script template with merge tags pulled from the Contact record — the merge tag is rendered as a coloured pill, e.g.:

> Hello, can I speak with **[Joey Cleint]** please?
>
> Hi **Joey Cleint**, this is Bob from ABC Fitness. We are hosting our 10th Annual Fitness Games and are hoping you can make it. Last year we had over 200 individuals participate, and we're looking to double that number this year!
>
> Are you interested in supporting a good cause and getting some great exposure for your business at the same time?

Single **Cancel** button (script is read-only).

### Schedule Follow-up modal
Triggered by `Schedule Callback ▾`. Layout: calendar on the left, time picker on the right.

| Element | Notes |
|---------|-------|
| Date | Month + Year dropdowns, Prev/Next links, Su–Sa grid |
| Hour | Two rows: AM `1–11 noon`, PM `1–11 midnight` |
| Minute | Grid `00–59` (5-minute increments highlighted in bold) |
| Follow-up on | Auto-computed datetime label, e.g. `Wednesday, Sep 14, 2016 at 12:00 AM` |
| Timezone | Footer text: `time is based on your timezone (-7 hrs from UTC/GMT)` |

Primary action: **Schedule Callback** (orange). Secondary: **Cancel** (blue).

### Connected Calls modal
Per-contact call history.

Columns: **Time · Phone Number · Duration · Mode** (Mode = `Dialer` / `Direct` / `conf`). Each row has a 👁 icon to view detail (likely opens recording).

Filter controls below the table:
- **Retrieve by Time** — dropdown: `hour, 2 hours, 4 hours, 8 hours, day, 2 days, 3 days`
- **Retrieve by No Calls** — alternative filter input

## See Also
- [intercloud9-dispositions.md](intercloud9-dispositions.md) — disposition catalogue
- [intercloud9-data-entities.md](intercloud9-data-entities.md) — Contact / CallRecord / ContactLog / ScheduledCallback / Script schemas
- [intercloud9-campaigns.md](intercloud9-campaigns.md) — where contacts come from
