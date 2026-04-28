# InterCloud9 — Agent Home Dashboard

Default landing page for any logged-in agent. Has four panels arranged 2 × 2.

**Source**: `intercloud9-dialer/knowledge_graph.json`
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Layout

```
┌──────────────────────────────────────────────────────────┐
│  Welcome, <Agent Name>!                                  │  ← orange banner
├──────────────────────────┬───────────────────────────────┤
│  Join a Predictive       │  Global Phone Search          │
│  Campaign                │  [search box] [Go]            │
│  · Business      View Stats                              │
│  · Consumer      View Stats                              │
│  · Test          View Stats                              │
├──────────────────────────┼───────────────────────────────┤
│  Scheduled Calls          │  My Stats                    │
│  · with Joey Cleint       │  [date range] [from][to][Get]│
│    interCloud9 12 in over │  Name: Demo                  │
│    12 day(s)              │  Agent Connect Time: 2031s   │
│    [eye][call][edit][O]   │  Agent Dialing Sessions: 37  │
│                           │  Contact Talk Time: 989s     │
│                           │  Connected Contacts: 6       │
│                           │  Attempted Direct Calls: 11  │
└──────────────────────────┴───────────────────────────────┘
```

## Panels

### Join a Predictive Campaign
Lists all campaigns the agent is allowed to join. Counter at top right shows total available (e.g. `3 Available Campaigns`). Each row has the campaign name as a link plus a **View Stats** link on the right.

### Scheduled Calls
Pending callbacks the agent has previously scheduled. Counter shows total. Each row has four action icons:
| Icon | Action |
|------|--------|
| 👁 eye (blue) | Open contact |
| 📞 phone (blue) | Call now |
| ✏️ pencil (orange) | Edit callback |
| ⊘ red O | Cancel callback |

Each row text follows the pattern: `with <First Name> <Last Name> <Company> in over <N> day(s)`.

### Global Phone Search
Full-width search box across **all campaigns** — find a contact by phone number to pull up its Contact View. Useful for inbound caller lookups.

### My Stats
| Field | Notes |
|-------|-------|
| Stats range | dropdown: `for Today` (others available) |
| From-date / To-date | date picker pair + **Get Custom** button |
| Name | agent's own display name |
| Agent Connect Time | seconds (with minutes/hours friendly text) |
| Agent Dialing Sessions | total + `(in-progress: N)` sub-count |
| Contact Talk Time | seconds |
| Connected Campaign Contacts | integer |
| Attempted Direct Calls | integer |

Bottom right of panel: **Display Agent Productivity** link (drilldown not captured).

## See Also
- [intercloud9-contact-view.md](intercloud9-contact-view.md) — what happens when an agent joins a campaign or opens a scheduled call
- [intercloud9-modules.md](intercloud9-modules.md) — full nav
