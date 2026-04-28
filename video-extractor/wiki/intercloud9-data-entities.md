# InterCloud9 — Data Entities

All entity fields and relationships inferred from the demo. Use this for DB schema design when cloning the product.

**Source**: `intercloud9-dialer/knowledge_graph.json`
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Entity Relationship Overview

```
User (Agent / Admin)
  ├── has many → CallRecord (as agent)
  ├── has many → ContactLog (as note author)
  └── ↔ Campaign (assignment, many-to-many)

Campaign
  ├── has many → Contact
  ├── has many → CallRecord
  ├── has many → Recording (via CallRecord)
  ├── has one  → Script (per campaign)
  └── ↔ User (assignment)

Contact
  ├── belongs to → Campaign
  ├── has many → CallRecord
  ├── has many → ContactLog
  └── has many → ScheduledCallback

CallRecord
  ├── belongs to → Contact
  ├── belongs to → Campaign  (nullable for Direct mode)
  ├── belongs to → User      (the agent)
  ├── has one  → Disposition (nullable → "Not Dispositioned")
  └── has one  → Recording

ScheduledCallback
  ├── belongs to → Contact
  ├── belongs to → User      (assigned agent)
  └── belongs to → Campaign

DoNotCallList   (consulted by Upload Contact "Scrub Against …")
  └── (standalone)
```

---

## User

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | auto |
| name | text | display name e.g. Demo, Adam |
| email_primary | email | |
| email_secondary | email | second email field shown in Admin |
| phone | phone | |
| connect_via | enum | `SIP Phone` \| `Telephone Dial-in` |
| sip_username | text | when SIP — e.g. `sip_2` |
| sip_password | text | when SIP — plaintext to admin |
| agent_id | text | when Dial-in — e.g. `sip_155` |
| pin | integer | when Dial-in — e.g. `1234` |
| role | enum | `Agent` \| `Admin` |

---

## Campaign

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | auto |
| name | text | required |
| description | text | |
| type | enum | `Predictive` (Edit modal title was "Edit Predictive Campaign"; other types likely exist) |
| caller_id_name | text | required — recipient sees this |
| caller_id_number | phone | required, validated |
| limit_calling_hours | boolean | |
| never_call_before | time | |
| never_call_after | time | |
| dial_rate_override | enum | `Auto` \| `Inbound` \| `1` \| `2` \| `3` \| `4` \| `5` |
| wait_for_agent | boolean | |
| abandon_rate | percent | computed; resettable |
| status | enum | Active / Paused (small status circle on card) |

---

## Contact

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | URL pattern: `/contact/3419513` |
| campaign_id | relate | → Campaign |
| business | text | context label, default `Unknown` |
| first_name | text | |
| last_name | text | |
| company | text | |
| address | text | |
| city | text | |
| state | text | |
| zip | text | |
| other | text | free-form |
| email | email | |
| lead_id | text | external lead-system reference |
| phone | phone | primary dial number |
| called_status | enum | `Uncalled` \| `Out of Time` \| `Called Once` (from pie chart) |
| current_disposition_id | relate | → Disposition |
| custom_fields | json | configurable via Admin → Setup Database Fields |

---

## CallRecord

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| contact_id | relate | → Contact |
| campaign_id | relate | → Campaign (nullable for Direct) |
| agent_id | relate | → User |
| phone_number | phone | |
| time | datetime | |
| duration_sec | integer | |
| mode | enum | `Dialer` \| `Direct` \| `conf` |
| disposition_id | relate | → Disposition (nullable) |
| recording_url | url | when Record was pressed |

---

## Disposition

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| name | text | |
| category | enum | `Made Contact` \| `Unable to Contact` \| `Custom` \| `System` |
| is_system | boolean | true for No Agent Available, Carrier Error NTF, Not Dispositioned |

**Known values**: see [intercloud9-dispositions.md](intercloud9-dispositions.md) for the catalogue.

---

## ScheduledCallback

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| contact_id | relate | → Contact |
| agent_id | relate | → User |
| campaign_id | relate | → Campaign |
| follow_up_at | datetime | |
| agent_timezone_offset | integer | e.g. `-7` (hours from UTC/GMT, displayed in modal) |
| created_at | datetime | |

---

## ContactLog

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| contact_id | relate | → Contact |
| date | datetime | shown as e.g. `16 Sep 16@11:25AM` |
| message | text | agent note OR auto-message |
| is_auto | boolean | true for `[auto]`-prefixed entries |
| agent_id | relate | → User (nullable when auto) |

---

## Script

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| campaign_id | relate | → Campaign |
| body | rich_text | supports merge tags pulling from Contact fields |
| popup_on_connect | boolean | mirrors the *Popup script on connect* checkbox |

---

## Recording

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| call_record_id | relate | → CallRecord |
| url | url | playable Website link |
| csv_url | url | bulk CSV export |
| direct_calls_only | boolean | tooltip *Recordings (Direct Calls Only)* implies this filter on the per-user Admin icon |

---

## DoNotCallList

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| phone_number | phone | |
| added_at | datetime | |
| scope | enum | `global` (national scrub) \| `campaign` (account-local) |

Consulted at Upload Contact time when **Scrub Against our Do-Not-Call List** is checked.

---

## See Also
- [intercloud9-modules.md](intercloud9-modules.md) — module overview
- [intercloud9-contact-view.md](intercloud9-contact-view.md) — Contact + CallRecord + ContactLog UX
- [intercloud9-campaigns.md](intercloud9-campaigns.md) — Campaign + Upload Contact flow
- [data-entities.md](data-entities.md) — MightyCall dialer entities for comparison
