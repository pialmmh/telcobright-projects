# UI Patterns

Common UI patterns observed across MightyCall's Auto Dialer, synthesized from all three video sources.

## Layout

- **Type**: Left navigation sidebar + main content area
- **Top navigation**: Workspace, Reports, Auto dialer (highlighted when active), Call flow, Numbers, Team, Integrations, Account
- **User status**: Top-right corner shows availability status (Available/Wrap-up) with timer and avatar

## Color Scheme

- **Primary**: Blue (#2563EB range)
- **Accent**: Green for active/enabled states
- **Background**: White/light gray
- **Status colors**: Green (Running, Available), Yellow (Ready, Paused), Red (Incomplete), Gray (Preparing)
- **Toggle states**: Green = ON, Gray = OFF

## Component Library

| Component | Usage |
|-----------|-------|
| Tab bar | Dialing mode selection (Preview/Progressive/Predictive/Agentless) |
| Wizard stepper | 4-step campaign creation (numbered, vertical left sidebar) |
| Data table | Campaigns list, record lists |
| Toggle switch | Local presence, DNC scrubber, AMD, Auto-rotation |
| Date picker | Start/end dates with calendar icon |
| Multi-select list | Business numbers with checkboxes |
| Three-dot menu | Campaign actions (Edit, Delete) |
| Avatar group | Agent assignment display |
| Badge/pill | Coverage score fraction + percentage |
| Tooltip | Feature explanations (Local Presence, DNC scrubber) |
| Modal/overlay | Campaign wizard, call outcome panel |
| Countdown timer | Wrap-up timer (e.g., "00:30") |

## Common Patterns

1. **Wizard with sidebar steps**: Numbered steps 1-4 in left sidebar, content area on right
2. **Inline tooltips**: Info icons that expand with detailed feature explanations
3. **Coverage score badges**: Fraction + percentage shown as colored indicators
4. **Status indicators**: Colored dots/icons + text labels for campaign states
5. **Action menus**: Three-dot (...) menus for row-level actions
6. **Panel overlays**: DNC scrubber panel slides in from top-right
7. **Confirmation timers**: Wrap-up countdown forces agent to select outcome
8. **Warning banners**: Yellow warnings about local presence coverage mismatches
9. **Upload zones**: Drag-and-drop areas for CSV file uploads
10. **Searchable lists**: "Search by label or number" for business numbers; "Search by list name" for record lists

## Mock Screen Reference

A pixel-faithful HTML mock of the Campaigns list screen is available as a styling reference:

**`../mock-screens/mightycall-campaigns.html`** — single self-contained HTML file, no dependencies.

Demonstrates all UI patterns in this page: sidebar, top nav, status badges, DNC panel, campaigns table with agent avatars, coverage score pills, action buttons.

Use this as the **baseline style guide** when building the actual dialer UI — copy the CSS variables, badge styles, and layout structure directly.

## Navigation Structure

```
Auto dialer (tab)
├── Campaigns (dropdown, default)
│   ├── Campaigns List
│   │   ├── Create campaign → Wizard (4 steps)
│   │   ├── Edit campaign → Same wizard
│   │   └── Campaign row actions (play/pause/stop/edit/delete)
│   └── DNC Panel (top-right)
│       ├── National DNC scrubber toggle
│       └── Local DNC List management
└── Lists (dropdown)
    └── Record list management
```
