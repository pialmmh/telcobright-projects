# Record Lists (Step 4)

Fourth step of the [Campaign Management](campaign-management.md) wizard. Manages the contact data that campaigns will dial.

## Upload

- **Method**: Upload or drag and drop a CSV file
- **Template**: "Download this template for guidance" link available
- **Size limit**: Files over 15 MB may take 5-7 minutes to upload
- **Format**: CSV with contact records

## Record List Panel

When selecting a list, the panel shows:

| Column | Description |
|--------|-------------|
| LIST NAME | Name of the uploaded CSV file |
| LAST CHANGES | User avatar + name, date/time of last modification |
| RECORDS | Number of records in the list |
| COVERAGE SCORE | Fraction (e.g., "0 of 1") + percentage, color-coded |

### Three-dot menu on uploaded list:
- **View** — inspect the list contents

## Available Lists (from demo data)

| List Name | Records | Area Codes | Coverage |
|-----------|---------|------------|----------|
| record_list_outbound campaign | 257 | 1 unique | — |
| full_list | 4,714 | 148 unique | — |
| outreach_LA (October) | 50 | 3 unique | — |
| LG4 leads - LG4 leads.csv | 296 | 98 unique | — |
| LA_new_leads | 48 | 3 unique | — |
| Gear10_discount_record_list | 48 | 3 unique | — |
| Cold_calls_record_list | 257 | 1 unique | Green dot |

## Coverage Score

Shows the percentage of unique contact area codes covered by your local and overlay business numbers.

- Displayed as fraction (e.g., "2 of 3") and percentage (e.g., "66.67%")
- Higher score = better [Local Presence](local-presence.md) effectiveness
- Low score triggers warning: "Local presence may be less effective if some client area codes aren't covered by your selected numbers"

## Customization

- **"Customize and upload more"** section for adding additional lists
- **"Add more"** button to upload additional CSV files
- **"New record list"** option at top of available lists

## Related

- [Local Presence](local-presence.md) — coverage score reflects local presence effectiveness
- [Campaign Management](campaign-management.md) — overall wizard context
- [DNC Compliance](dnc-compliance.md) — lists are scrubbed against DNC registries
