# Data Entities

Core data objects in MightyCall's Auto Dialer, synthesized from all three video sources.

## Campaign

The central entity. Contains all configuration for an outbound calling effort.

| Field | Type | Description |
|-------|------|-------------|
| name | string | Campaign display name |
| description | string | Optional, max 200 chars |
| status | enum | Preparing, Scheduled, Ready, Running, Paused, Completed, Incomplete |
| timezone | string | e.g., "UTC-06:00 Central Time" |
| start_date | date | Optional scheduled start |
| end_date | date | Optional scheduled end |
| business_hours | object[] | Per-day schedule (day, start, end, full_day) |
| dialer_mode | enum | Preview, Progressive, Predictive, Agentless |
| business_numbers | reference[] | Selected Business Numbers |
| auto_rotation | boolean | Rotate through numbers |
| local_presence | boolean | Match caller ID to area code |
| agents | reference[] | Assigned agents |
| record_list | reference | Uploaded contact list |

**Relationships**: has many → Agents, has one → Record List, has one → Dialer Settings, has many → Business Numbers

## Dialer Settings

Mode-specific configuration, embedded within Campaign.

### Preview Mode Fields
| Field | Type | Description |
|-------|------|-------------|
| preview_time | integer (sec) | Agent review time before call |
| wrap_up_time | integer (sec) | Post-call wrap-up duration |
| max_ring_time | integer (sec) | Ring duration before timeout |
| default_retry_period | integer (min) | Wait between retries |
| max_attempts_per_record | integer | Max calls per contact |

### Progressive Mode Fields
| Field | Type | Description |
|-------|------|-------------|
| auto_answer_timeout | integer (sec) | Default: 3 |
| ringing_agent_time | integer (sec) | Default: 30 |
| wrap_up_time | integer (sec) | Default: 30 |
| max_ring_time | integer (sec) | Default: 25 |
| default_retry_period | integer (min) | Default: 30 |
| max_attempts_per_record | integer | Default: 3 |
| answering_machine_detection | boolean | Default: ON |

### Predictive Mode Fields
| Field | Type | Description |
|-------|------|-------------|
| lines_per_agent | integer | Simultaneous calls ratio |
| wrap_up_time | integer (sec) | Post-call duration |
| max_ring_time | integer (sec) | Ring timeout |
| default_retry_period | integer (min) | Retry wait |
| max_attempts_per_record | integer | Max attempts |
| answering_machine_detection | boolean | AMD toggle |

## System Disposition

Auto-determined call outcomes with retry logic.

| Field | Type | Description |
|-------|------|-------------|
| name | string | e.g., "Contact busy" |
| retry_period | integer (min) | Wait before retry |
| attempts_per_number | integer | Max retries |
| action | enum | Retry or Final |

## Agent Disposition

Manual call outcomes selected by agents.

| Field | Type | Description |
|-------|------|-------------|
| name | string | e.g., "Successful call" |
| action | enum | Retry or Final |

## Record List

CSV-based contact data uploaded to campaigns.

| Field | Type | Description |
|-------|------|-------------|
| name | string | Filename or custom name |
| records | integer | Number of contacts |
| unique_area_codes | integer | Distinct area codes |
| coverage_score | object | { covered: int, total: int, percentage: float } |
| last_changed_by | string | User who last modified |
| last_changed_at | datetime | Last modification time |

## Business Number

Phone numbers available for outbound calling.

| Field | Type | Description |
|-------|------|-------------|
| label | string | e.g., "LA Main" |
| number | string | e.g., "+1 713 647 2453" |
| type | enum | Local, Toll-Free |

## DNC List

Do Not Call registry (local/internal).

| Field | Type | Description |
|-------|------|-------------|
| numbers | string[] | Blocked phone numbers |
| count | integer | Total numbers in list |
| type | enum | National (external), Local (internal) |

## Entity Relationships

```
Campaign ──has one──▶ Dialer Settings
Campaign ──has many──▶ Business Number
Campaign ──has one──▶ Record List
Campaign ──has many──▶ Agent
Campaign ──has many──▶ System Disposition
Campaign ──has many──▶ Agent Disposition
Record List ──scrubbed by──▶ DNC List
Agent ──selects──▶ Agent Disposition
Agent ──can add to──▶ DNC List
```
