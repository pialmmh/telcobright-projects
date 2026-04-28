# InterCloud9 vs MightyCall — Concept Mapping

Both products are predictive auto-dialers; this page maps the InterCloud9 demo's concepts onto the MightyCall wiki already in this repo so an implementer can pick from either pattern.

**Sources**: `intercloud9-dialer/knowledge_graph.json` · `crm-mightycall/knowledge_graph.json` · `preview-dialer/knowledge_graph.json` · `progressive-dialer/knowledge_graph.json`
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Identical concepts

| Concept | Both products do this |
|---------|-----------------------|
| Predictive dialing | Same idea — system over-dials based on agent availability |
| Campaign-as-container | Each campaign owns Caller ID, hours, contacts, recordings |
| CSV upload + column mapping | Almost identical UX (mapper + preview rows) |
| DNC scrub at upload | Same checkbox, same TCPA gate ("I am Allowed to Call These Contacts") |
| Disposition split (system vs agent) | Same model |
| Per-agent recording playback | Both surface a Recordings link |
| Real-time supervisor monitor | Both have a live agent table with barge controls |

## Differences

| Aspect | MightyCall | InterCloud9 |
|--------|-----------|-------------|
| **Workspace shape** | Two screens — separate List View and agent screen | One screen — `Contact View` is form + dialer + log + script all in one |
| **Connection method** | (Not detailed in docs) | Per-user choice: **SIP Phone** *or* **Telephone Dial-in** with separate credential schema |
| **Dial Rate control** | Mode-specific — Predictive auto-tunes | Per-campaign **Dial Rate Override** dropdown: `Auto · Inbound · 1–5` |
| **Wait for Agent** | Implicit by mode | Explicit campaign checkbox |
| **Script delivery** | Not surfaced in MightyCall wiki | First-class **Read Script** modal with merge tags rendered as coloured pills, plus *Popup script on connect* toggle |
| **Disposition UI** | Flat list of buttons | 5 buckets × dropdowns (Custom · Schedule Callback · Made Contact · Unable to Contact · Assign to) |
| **Stats (per agent)** | Coverage Score on List | "My Stats" panel on Home with date range, plus Display Agent Productivity link |
| **Coaching keypad** | (Not documented in MightyCall wiki) | DTMF codes — `2` whisper, `1` takeover, `3` conference |
| **Lead ID field** | Not present | First-class field on Contact for external lead-system cross-ref |
| **Modal Recordings filter** | (Not surfaced) | `Recordings (Direct Calls Only)` per-user — campaign recordings live elsewhere |

## Naming map

| MightyCall term | InterCloud9 term |
|-----------------|------------------|
| Agent Workspace | Contact View |
| Campaign Wizard step 4 (CSV Upload) | Upload Contact modal |
| Coverage Score | (No direct analogue — see "Remaining Contacts: X (Y available)") |
| List View (record list) | List View (referenced; not detailed) + Contact View (worked one at a time) |
| Disposition (system) | Calling Data dispositions (No Agent Available, Carrier Error NTF, Not Dispositioned) |
| Disposition (agent) | Disposition Bar buckets |
| Local Presence (area-code matching) | Not demonstrated in 4:40 demo |

## When to pick which model when building

- **Build like MightyCall** when you want a clean separation of supervisor/agent concerns and you don't need an embedded script.
- **Build like InterCloud9** when agents need everything (form + dialer + script + history) on one screen, and the deployment supports both SIP softphones and telephone dial-in agents.

## See Also
- [intercloud9-modules.md](intercloud9-modules.md)
- [intercloud9-contact-view.md](intercloud9-contact-view.md)
- [campaign-management.md](campaign-management.md) — MightyCall campaign wizard
- [dialing-modes.md](dialing-modes.md) — MightyCall mode comparison
- [dispositions.md](dispositions.md) — MightyCall disposition split
