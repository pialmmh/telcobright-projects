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

## Mock Screen & Styling Reference

A working HTML mock of the Campaigns list is at **`../mock-screens/mightycall-campaigns.html`** — single file, no dependencies. Use it as the **CSS and layout baseline** for all dialer screens.

### Design Tokens

```css
/* Colors */
--primary:        #2563eb;   /* buttons, active nav, avatar bg */
--primary-hover:  #1d4ed8;
--sidebar-bg:     #1e3a5f;   /* dark navy left sidebar */
--body-bg:        #f3f4f6;   /* page background */
--card-bg:        #ffffff;
--border:         #e5e7eb;
--text:           #111827;
--text-muted:     #6b7280;

/* Status badge colors */
--running-bg:     #dcfce7;  --running-text:    #15803d;
--paused-bg:      #fef9c3;  --paused-text:     #a16207;
--ready-bg:       #fef9c3;  --ready-text:      #a16207;
--scheduled-bg:   #dbeafe;  --scheduled-text:  #1d4ed8;
--incomplete-bg:  #fee2e2;  --incomplete-text: #b91c1c;
--completed-bg:   #f3f4f6;  --completed-text:  #6b7280;
--preparing-bg:   #f3f4f6;  --preparing-text:  #9ca3af;

/* Dialing mode chip colors */
--predictive-bg:   #ede9fe;  --predictive-text:   #5b21b6;
--progressive-bg:  #dbeafe;  --progressive-text:  #1e40af;
--preview-bg:      #dcfce7;  --preview-text:      #065f46;
--agentless-bg:    #f3f4f6;  --agentless-text:    #374151;

/* Sizing */
--sidebar-width:  60px;
--topnav-height:  52px;
--radius-card:    12px;
--radius-btn:     8px;
--radius-badge:   20px;
```

### Layout Structure

```
body (display:flex, height:100vh)
├── aside.sidebar      (60px wide, dark navy, icon nav + avatar at bottom)
└── div.main           (flex:1, flex-direction:column)
    ├── nav.topnav     (52px tall, white, border-bottom, tabs + status pill)
    └── div.page-body  (flex:1, overflow-y:auto, padding:24px, bg:#f3f4f6)
        ├── .page-header   (title left, action buttons right)
        ├── .dnc-panel     (white card, horizontal row of DNC controls)
        └── .card > table  (campaigns table, white bg, rounded-12px)
```

### Key Component CSS Patterns

**Status badge** — pill with colored dot:
```css
.status-badge { display:inline-flex; align-items:center; gap:6px;
  padding:4px 10px; border-radius:20px; font-size:12px; font-weight:600; }
```

**Agent avatar group** — overlapping circles:
```css
.avatars { display:flex; }
.avatar  { width:28px; height:28px; border-radius:50%; border:2px solid #fff;
  margin-left:-6px; font-size:10px; font-weight:700; color:#fff; }
.avatars .avatar:first-child { margin-left:0; }
```

**Coverage score pill**:
```css
.cov-pill { padding:3px 8px; border-radius:12px; font-size:12px; font-weight:600; }
.cov-good { background:#dcfce7; color:#15803d; }   /* ≥80% */
.cov-warn { background:#fef9c3; color:#a16207; }   /* <80% */
```

**Toggle switch** (DNC / Local Presence / AMD):
```css
.toggle { width:40px; height:22px; border-radius:11px; background:#16a34a; position:relative; }
.toggle::after { content:''; position:absolute; width:18px; height:18px;
  border-radius:50%; background:#fff; top:2px; right:2px; }
.toggle.off { background:#d1d5db; }
.toggle.off::after { right:auto; left:2px; }
```

**Row action buttons** — contextual by status:
```css
.action-btn       { width:30px; height:30px; border-radius:6px; border:1px solid #e5e7eb; }
.action-btn.play  { color:#16a34a; border-color:#bbf7d0; background:#f0fdf4; }
.action-btn.pause { color:#ca8a04; border-color:#fef08a; background:#fefce8; }
.action-btn.stop  { color:#dc2626; border-color:#fecaca; background:#fef2f2; }
```

**User availability pill** (top-right):
```css
.status-pill { display:flex; align-items:center; gap:6px; background:#f0fdf4;
  border:1px solid #bbf7d0; border-radius:20px; padding:4px 12px;
  font-size:12px; font-weight:600; color:#16a34a; }
```

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
