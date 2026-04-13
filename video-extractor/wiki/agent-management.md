# Agent Management

## Agent List (Step 3)

Third step of the [Campaign Management](campaign-management.md) wizard. Assign agents to the campaign.

- Agents are shown as avatars in the campaigns list
- Multiple agents can be assigned per campaign
- A campaign needs at least one agent to move from "Preparing" to "Ready" status (except [Agentless](dialing-modes.md) mode)

## Agent Workspace

The agent workspace is where agents handle calls during an active campaign. Accessed via the **Workspace** tab in the top navigation.

### Layout

**Left Panel — Contact List:**
- Tabs: Unanswered, My recents, Clients, Team
- Shows: Internal toggle
- Each contact shows: name, status icon, last activity description, timestamp
- Contact statuses observed: Ongoing outbound call, Dropped inbound call, Connected outbound call, Voicemail

**Center Panel — Conversation Thread:**
- Chat-style message history with timestamps
- Supports: text messages, images, notes
- Call recordings shown inline: "Connected call..." with duration, play button
- "Didn't connect..." entries for failed calls with recording

**Right Panel — Call Outcome (during wrap-up):**
- Header: "SELECT CALL OUTCOME"
- Options: see [Dispositions](dispositions.md)
- Contact phone number displayed (e.g., +1 904 515 4645)
- Checkbox: "Add the number to Do not call list" — see [DNC Compliance](dnc-compliance.md)

### Agent Status

- Shows in top-right: status indicator + timer
- Observed status: "Wrap-up 00:30" (countdown timer during wrap-up period)
- Wrap-up time is configured per [Dialing Mode](dialing-modes.md) in [Dialer Settings](dialer-settings.md)

### Call Outcome Flow

1. Call completes → agent enters Wrap-up state
2. Timer counts down (e.g., 00:30)
3. Agent selects call outcome from [Dispositions](dispositions.md)
4. Optionally checks "Add to DNC list"
5. Agent becomes available for next call

## Related

- [Dispositions](dispositions.md) — call outcome options
- [DNC Compliance](dnc-compliance.md) — agent-level DNC checkbox
- [Dialing Modes](dialing-modes.md) — how agent interaction differs by mode
