# DNC Compliance

MightyCall's Do Not Call compliance features help reduce the risk of TCPA and DNC violations and lawsuits. Visible on the [Campaigns List](campaign-management.md) page in the top-right corner.

## National DNC List Scrubber

- **Toggle**: ON/OFF switch on the campaigns list page
- **What it does**: Integrates with external scrubbing services to verify dialing lists against federal "Do Not Call" lists
- **When enabled**: Automatically removes registered numbers from campaign lists before dialing
- **Purpose**: Reduce the risk of TCPA and DNC violations and lawsuits

> "MightyCall is integrated with the scrubbing services to verify your dialing lists against 'Do Not Call' lists and reduce the risk of TCPA and DNC violations and lawsuits."

## Local DNC List (Internal)

A per-account internal Do Not Call list that blocks specific numbers across all campaigns.

### Management Options
Accessible via the Local DNC List dropdown menu:

| Action | Description |
|--------|-------------|
| **Add more** | Upload additional numbers to the DNC list |
| **Replace** | Replace the entire list with a new upload |
| **Delete all** | Remove all numbers from the local DNC list |
| **Export to CSV** | Download the current list as a CSV file |

The UI shows the count of numbers in the list (e.g., "2 NUMBERS").

## Agent-Level DNC

Agents can add numbers to the Internal DNC list directly after a call by checking the **"Add the number to Do not call list"** checkbox in the [Agent Workspace](agent-management.md) call outcome panel. This provides a real-time way for agents to flag numbers that should not be called again.

See also: [Dispositions](dispositions.md) for the full call outcome flow.

## Compliance Summary

| Layer | Scope | How Applied |
|-------|-------|-------------|
| National DNC Scrubber | Federal registry | Automatic, pre-dialing |
| Local DNC List | Account-wide | Automatic, blocks across all campaigns |
| Agent DNC checkbox | Per-call | Manual, agent adds during wrap-up |
