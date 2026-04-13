# General Settings (Step 1)

First step of the [Campaign Management](campaign-management.md) wizard. Identical across all [Dialing Modes](dialing-modes.md).

## Fields

| Field | Type | Required | Details |
|-------|------|----------|---------|
| Campaign Name | Text input | Yes | Free text, appears in campaigns list |
| Description | Textarea | No | 0/200 character limit |
| Timezone | Dropdown | Yes | Default: "UTC-06:00 Central Time (US & Canada)", option for "Profile time zone" |
| Start Date | Date picker | No | mm/dd/yyyy format, shows days remaining badge (e.g., "13 days") |
| End Date | Date picker | No | mm/dd/yyyy format |
| Business Hours | Day schedule | No | Sunday-Saturday, each with start time, end time, AM/PM toggle, "Full day" checkbox. Monday-Friday checked by default. Default hours: 08:00-09:00 |
| Business Numbers | Multi-select list | Yes | Select from account's numbers. "+" button to add more |
| Auto-rotation | Toggle | No | Rotate through selected business numbers |
| [Local Presence](local-presence.md) | Toggle | No | Match caller ID to contact's area code |

## Business Numbers Available (from demo)

| Label | Number |
|-------|--------|
| LA Main | +1 713 647 2453 |
| LA Sales | +1 323 522 5554 |
| NYC | +1 332 213 9228 |
| Toronto | +1 647 361 5305 |
| San Diego | +1 650 300 0672 |
| Toll-Free | +1 855 855 9875 |
| Toll-Free | +1 888 388 0889 |

## Business Hours Configuration

Each day row has:
- Checkbox to enable/disable that day
- Start time (HH:MM)
- AM/PM toggle
- End time (HH:MM)
- AM/PM toggle
- "Full day" checkbox

This helps prevent calling prospects at wrong times, improving connectivity and compliance.

## Navigation

Clicking "Cancel" discards changes. Clicking "Save" saves the campaign (moves to next step or saves all steps).
