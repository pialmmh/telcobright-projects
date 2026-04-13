# Local Presence

A feature in [General Settings](general-settings.md) that automatically matches the outbound caller ID to the contact's area code, making calls appear local and increasing answer rates.

## How It Works

1. When enabled, the system checks the contact's phone number area code
2. Selects the best matching business number from your selected numbers
3. Calls are distributed evenly among matching numbers
4. If no match is found, the Auto Dialer uses all selected numbers

## Configuration

- **Toggle**: ON/OFF in General Settings (Step 1)
- **Label**: "Local Presence"
- **Description**: "Selects the best business number based on the contact's area code"

## Behavior Details

From the tooltip:
- Feature uses **only** business numbers that match the contact's location
- Some selected numbers may not be used if they don't match any contacts
- Calls are distributed evenly among matching numbers
- If no match is found, Auto Dialer uses **all** selected numbers (fallback)

## Warnings

- Using all numbers (no match) may hurt business numbers' reputation and lower answer rates
- It is recommended to purchase additional numbers that match contact locations
- [Record Lists](record-lists.md) show a warning when "Local presence may be less effective if some client area codes aren't covered by your selected numbers. Consider adding more matching ones."

## Coverage Score Relationship

The [Coverage Score](record-lists.md) on record lists shows the percentage of unique contact area codes covered by your local and overlay numbers. A higher coverage score means Local Presence will be more effective.

## Related

- [General Settings](general-settings.md) — where Local Presence is configured
- [Record Lists](record-lists.md) — coverage score reflects Local Presence effectiveness
- [Campaign Management](campaign-management.md) — overall campaign setup
