# InterCloud9 — Dispositions

Call outcomes — split into agent-applied and system-applied. The same catalogue is referenced from Contact View (apply), Campaigns Export (filter), and Graph Stats (chart segments).

**Source**: `intercloud9-dialer/knowledge_graph.json` (frames 0079, 0204, 0217)
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Agent-applied dispositions (Disposition Bar)

Set from the **Disposition Bar** in Contact View. Five buckets, each a dropdown of sub-values.

| Bucket | Sub-values (observed) | Meaning |
|--------|-----------------------|---------|
| **Custom ▾** | (user-defined per account) | Tenant-defined extras |
| **Schedule Callback ▾** | Schedule a follow-up | Triggers Schedule Follow-up modal |
| **Made Contact ▾** | Direct Call · Inbox · Sale/Goal/Lead | Spoke with the right person |
| **Unable to Contact ▾** | No Contact · Wrong Number · Machine Left Msg · Not Interested/Dead | Did not / cannot complete |
| **Assign to ▾** | Reassign to another agent (closer/specialist) | Ownership change |

## System dispositions (Calling Data)

Applied automatically by the dialer engine. Observed in the Graph Stats → *Calling Data* tab:

| Disposition | Cause | Counts toward |
|-------------|-------|---------------|
| **No Agent Available** | Predictive over-dialed; no agent free when contact answered | Abandon Rate |
| **Not Dispositioned** | Agent moved on without selecting a disposition | Quality flag |
| **Carrier Error NTF** | *Number That Failed* — telco rejected the dial | Skip on retry |

## Full catalogue (from Export modal)

The Campaigns → Export Contacts modal exposes the complete agent-side disposition list as filterable checkboxes:

- Direct Call
- Inbox
- Scheduled Callback
- Sale/Goal/Lead
- Not Interested/Dead
- No Contact
- Wrong Number
- Machine Left Msg

## Comparison with MightyCall

InterCloud9's split is similar to MightyCall's *system vs agent* model documented in [dispositions.md](dispositions.md), but the bucket organisation differs:

| Aspect | MightyCall | InterCloud9 |
|--------|-----------|-------------|
| System dispositions | Standalone class — set by AMD, busy detector, etc. | Split into "Calling Data" (No Agent Available, Carrier Error NTF, Not Dispositioned) |
| Agent dispositions | Flat list, fully tenant-configurable | Two-level: bucket dropdown → sub-value |
| TCPA enforcement | Same — DNC scrub at upload | Same — scrub-on-upload + I am Allowed checkbox |

## See Also
- [intercloud9-contact-view.md](intercloud9-contact-view.md) — where dispositions are applied
- [intercloud9-campaigns.md](intercloud9-campaigns.md) — Export and Graph Stats modals
- [dispositions.md](dispositions.md) — MightyCall analogue
