# Dialer Settings (Step 2)

Second step of the [Campaign Management](campaign-management.md) wizard. Configuration varies by [Dialing Mode](dialing-modes.md).

## Mode Selection

Tab bar at top: **Preview** | **Progressive** | **Predictive** | **Agentless**

Each tab shows a brief description:
- Preview: "For small teams, manual review"
- Progressive: "For small to medium teams, steady flow"
- Predictive: "For large teams, max. efficiency, min. idle time"
- Agentless: "No agents, great for automation"

## Settings by Mode

### Preview Mode
| Setting | Default | Description |
|---------|---------|-------------|
| Preview time | — | How long agent can review contact info before call |
| Wrap-up time | — | Time after call for agent to complete notes |
| Max ring time | — | How long to ring before giving up |
| Default retry period | — | Wait time before retrying failed contacts |
| Max attempts per record | — | Maximum call attempts per contact number |

### Progressive Mode
| Setting | Default | Description |
|---------|---------|-------------|
| Auto answer timeout | 3 sec | Time before auto-connecting agent to answered call |
| Ringing agent time | 30 sec | How long to ring the agent |
| Wrap-up time | 30 sec | Time after call for agent to complete notes |
| Max ring time | 25 sec | How long to ring the contact |
| Default retry period | 30 min | Wait time before retrying failed contacts |
| Max attempts per record | 3 | Maximum call attempts per contact number |
| Answering Machine Detection | ON | Detect and handle answering machines |

### Predictive Mode
| Setting | Default | Description |
|---------|---------|-------------|
| Lines per agent | — | Ratio of simultaneous outbound calls per agent |
| Wrap-up time | — | Time after call for agent to complete notes |
| Max ring time | — | How long to ring the contact |
| Default retry period | — | Wait time before retrying |
| Max attempts per record | — | Maximum call attempts per contact |
| Answering Machine Detection | ON | Detect and handle answering machines |

## Dispositions

See [Dispositions](dispositions.md) for full details. Configured in this step.

## Key Differences Between Modes

1. **Auto answer** — Progressive and Predictive only (not Preview)
2. **AMD** — Progressive and Predictive only (not Preview)
3. **Preview time** — Preview only (replaced by "Ringing agent time" in Progressive)
4. **Lines per agent** — Predictive only
5. System dispositions differ by mode (see [Dispositions](dispositions.md))
