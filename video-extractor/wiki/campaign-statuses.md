# Campaign Statuses

Campaigns in the [Campaigns List](campaign-management.md) display one of seven statuses.

## Status Definitions

| Status | Icon Color | Meaning | Can Edit? | Can Delete? |
|--------|-----------|---------|-----------|-------------|
| **Preparing** | Gray (--) | Business number, agent, or record list hasn't been assigned yet | Yes (full) | Yes |
| **Scheduled** | Green | Campaign is set to start at a future date | Yes (full) | Yes |
| **Ready** | Yellow | Fully configured, ready to start | Yes (full) | Yes |
| **Running** | Green (animated) | Campaign is currently active | Limited | No |
| **Paused** | Yellow | Temporarily stopped | Limited | Yes |
| **Completed** | Green (checkmark) | Campaign has finished | No | Yes |
| **Incomplete** | Red | Missing required configuration (similar to Preparing) | Yes (full) | Yes |

## Edit Restrictions

**Full edit** (Preparing, Scheduled, Ready, Incomplete):
- All 4 steps of the wizard can be modified

**Limited edit** (Running, Paused):
- General settings: editable
- Dialer settings: limited changes for Progressive and Predictive modes
- Agent list: editable
- Record list: restricted

**No edit** (Completed):
- Campaign is locked, cannot be modified

## Status Transitions

```
Preparing → Scheduled (when start date is in future)
Preparing → Ready (when all required fields filled, no future start date)
Scheduled → Running (when start date/time arrives)
Ready → Running (user clicks play)
Running → Paused (user clicks pause)
Paused → Running (user clicks play)
Running → Completed (all records processed or end date reached)
```

## Controls

Each campaign row has play/pause/stop controls on the left side for managing the campaign state.

## Related

- [Campaign Management](campaign-management.md) — overall campaign lifecycle
