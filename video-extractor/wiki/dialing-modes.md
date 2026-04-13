# Dialing Modes

MightyCall's Auto Dialer supports four dialing modes, selected in Step 2 (Dialer Settings) of the campaign wizard.

## Mode Comparison

| Feature | Preview | Progressive | Predictive | Agentless |
|---------|---------|-------------|------------|-----------|
| **Team size** | Small teams | Small-medium teams | Large teams | No agents |
| **Call initiation** | Agent manually initiates | System auto-initiates | System auto-initiates (ratio-based) | System auto-initiates |
| **Agent reviews contact first?** | Yes | No | No | No |
| **Auto answer** | No | Yes (timeout configurable, default 3s) | Yes | N/A |
| **Answering Machine Detection** | No | Yes (toggle) | Yes | Yes |
| **Agent control** | Highest | Medium | Lowest | None |
| **Efficiency** | Lowest | Medium | Highest | Automated |
| **Preview time setting** | Yes | No (replaced by Ringing agent time) | No | No |
| **Key timing settings** | Preview time, Wrap-up time, Max ring time | Ringing agent time, Wrap-up time, Max ring time | Lines per agent, Wrap-up time, Max ring time | N/A |

## Preview Dialing
*Source: [preview-dialer](../preview-dialer/knowledge_graph.json)*

> "Agent is provided with a preview of the contact's information before initiating the call."

- Best for: small teams, manual review, high-value leads
- Agent sees contact details before the call is placed
- Agent decides when to initiate the call
- Preview time defines how long the agent can review contact information
- Unique settings: Preview time
- System dispositions: Contact busy, Contact no response, Agent abandoned, Invalid number, Blocked by spam filters, Blocked by robocall analytics

## Progressive Dialing
*Source: [progressive-dialer](../progressive-dialer/knowledge_graph.json)*

> "The Progressive campaign automatically initiates calls, allowing agents to connect with contacts who are already on the line, making it a more efficient option compared to Preview mode."

- Best for: small-to-medium teams, steady call flow
- System automatically dials the next contact when an agent becomes available
- Agent connects only to answered calls (no manual initiation)
- More efficient than Preview but less agent control
- Unique settings: Auto answer (3s default timeout), Answering Machine Detection toggle, Ringing agent time (30s default)
- System dispositions: Contact busy, Contact no response, Contact abandoned, Invalid number, Answering machine (when AMD enabled)

## Predictive Dialing
*Source: [crm-mightycall](../crm-mightycall/knowledge_graph.json)*

- Best for: large teams, maximum efficiency, minimum idle time
- System dials multiple numbers simultaneously based on predicted agent availability
- Uses lines-per-agent ratio to optimize throughput
- Highest efficiency but lowest agent control
- Unique settings: Lines per agent ratio, Answering Machine Detection
- System dispositions: Contact busy, Contact no response, Agent abandoned, Invalid number, Answering machine

## Agentless Dialing
*Source: mentioned in all three videos*

- No agents required — great for automation
- Used for pre-recorded messages, surveys, or notifications
- System dials contacts and plays automated content

## Shared Across All Modes

All modes share the same:
- [General Settings](general-settings.md) (Step 1)
- [Agent List](agent-management.md) (Step 3, except Agentless)
- [Record List](record-lists.md) (Step 4)
- [DNC Compliance](dnc-compliance.md) features
- [Campaign Statuses](campaign-statuses.md)
- [Agent Dispositions](dispositions.md) (Successful call, Call back later, Incorrect number, Not interested, Left voicemail)
