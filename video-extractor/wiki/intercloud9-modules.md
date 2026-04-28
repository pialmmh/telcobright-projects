# InterCloud9 Predictive Dialer — Modules Overview

Cloud-based predictive auto-dialer demoed at `pd.intercloud9.com`. Browser-only agent UI; supervisors monitor and barge live; admins configure users and campaigns.

**Source**: `intercloud9-dialer/knowledge_graph.json`
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Top Navigation

`Home · List View · Contact View · Settings · Admin · Campaigns · Agent Monitor`

The active item is highlighted with a darker blue pill. Right side of the header always shows server response time (e.g. `87ms`) and **Logout**.

## Modules at a glance

| Module | URL | Audience | Purpose |
|--------|-----|----------|---------|
| [Home](intercloud9-agent-home.md) | `/#/home` | Agent | Join campaigns, see scheduled callbacks, personal stats |
| List View | `/#/list` | Agent / Supervisor | Bulk contact view (referenced; not detailed in this video) |
| [Contact View](intercloud9-contact-view.md) | `/#/contact/[id]` | Agent | Active call workspace — form, dialer, disposition, script |
| Settings | `/#/settings` | All | Per-user preferences (referenced; not detailed) |
| [Admin](intercloud9-admin.md) | `/#/admin` | Admin | User provisioning, custom contact fields |
| [Campaigns](intercloud9-campaigns.md) | `/#/campaign` | Admin / Supervisor | Create, edit, upload contacts, monitor stats, export |
| [Agent Monitor](intercloud9-agent-monitor.md) | `/#/monitor` | Supervisor | Live agent status, barge / coach / conference, recordings |

## Cross-module features

- **Disposition system** is shared across Contact View (apply), Campaigns Export (filter), and Graph Stats (chart legend). See [intercloud9-dispositions.md](intercloud9-dispositions.md).
- **DNC scrubbing** is applied once at Upload Contact time — every campaign upload has the *Scrub Against our Do-Not-Call List* checkbox plus the TCPA *I am Allowed to Call These Contacts* gate.
- **Recording playback** is reachable from three places: Contact View (per-call), Agent Monitor → Recorded Calls tab (per-agent), and Campaigns row → *Recordings: Website / CSV* (per-campaign export).
- **Agent stats** are mirrored: Home → *My Stats* (self), Admin → per-user *Stats* icon, Agent Monitor → live state per agent.
- **Scheduled callbacks** created in Contact View show up on the Home page regardless of which campaign produced them.

## See Also
- [intercloud9-data-entities.md](intercloud9-data-entities.md) — full schema
- [intercloud9-dispositions.md](intercloud9-dispositions.md) — disposition catalogue
- [intercloud9-vs-mightycall.md](intercloud9-vs-mightycall.md) — comparison with the existing MightyCall dialer wiki
