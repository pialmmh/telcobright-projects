# Dispositions

Call outcome classifications used in [Dialer Settings](dialer-settings.md). Two types: System (automatic) and Agent (manual).

## System Dispositions

Automatically determined by the system based on call result. Each has configurable retry period, attempts per number, and Retry/Final classification.

| Disposition | Preview | Progressive | Predictive | Action | Description |
|-------------|---------|-------------|------------|--------|-------------|
| Contact busy | Yes | Yes | Yes | Retry | Contact's line is busy |
| Contact no response | Yes | Yes | Yes | Retry | Contact didn't answer |
| Contact/Agent abandoned | Yes | Yes | Yes | Retry | Call was abandoned |
| Invalid number | Yes | Yes | Yes | Final | Number is invalid |
| Blocked by spam filters | Yes | No | No | Final | Call blocked by spam filter |
| Blocked by robocall analytics | Yes | No | No | Final | Call blocked by robocall detection |
| Answering machine | No | Yes (when AMD on) | Yes | Final | Answering machine detected |

### Retry Configuration
For dispositions marked "Retry":
- **Retry period**: time to wait before retrying (e.g., 30 min)
- **Attempts per num**: max retry attempts for that number (e.g., 3)

### Final vs Retry
- **Retry**: System will attempt to call the number again after the retry period
- **Final**: Number is removed from the active calling queue, no further attempts

## Agent Dispositions

Manually selected by agents after a call is completed. Shown in the [Agent Workspace](agent-management.md) as "SELECT CALL OUTCOME" panel.

| Disposition | Action | Description |
|-------------|--------|-------------|
| Successful call | Final | Call achieved its objective |
| Call back later | Final | Contact requested a callback |
| Incorrect number | Final | Wrong number reached |
| Not interested | Final | Contact declined |
| Left voicemail | Final | Voicemail was left |
| Already a customer | Final | Contact is already a customer (Preview only) |
| Left unanswered | Final | No answer, no voicemail (Preview only) |

## Agent DNC Integration

During disposition selection, agents can also check **"Add the number to Do not call list"** to add the contact's number to the [Internal DNC List](dnc-compliance.md) directly. This appears as a checkbox below the phone number in the call outcome panel.
