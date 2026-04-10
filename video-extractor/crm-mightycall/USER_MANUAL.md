# MightyCall Predictive Dialer User Manual

*Auto-generated from video demonstration*

## Overview

This documentation covers the features demonstrated in the MightyCall Predictive Dialer video.

## Modules

### Auto Dialer

Outbound calling automation module. Contains campaign management and record list management. Accessible via top navigation 'Auto dialer' tab.

### Reports

Analytics and performance reporting for outbound campaigns. Shows campaign metrics, agent sessions, dispositions and call details.

## Features

### Campaign Management

**Module**: auto_dialer  
**Type**: workflow

Create, manage and monitor outbound calling campaigns. Campaigns can be in states: Running, Ready, Completed, Paused, Incomplete.

**Steps**:
1. Navigate to Auto Dialer > Campaigns
2. Click 'Create campaign' button
3. Fill in General Settings (name, description, timezone, dates, business hours, phone numbers)
4. Configure Dialer Settings (choose dialer mode and mode-specific parameters)
5. Add agents to Agent List
6. Upload or select a Record List
7. Save and launch campaign

**Business Value**: Enables teams to run structured outbound calling campaigns with full control over scheduling, staffing, and contact lists.

---

### Predictive Dialing Mode

**Module**: auto_dialer  
**Type**: configuration

Algorithm-driven mass calling for large teams. Maximizes call efficiency and reduces agent idle time. At campaign start, algorithm collects statistics to make accurate predictions. Dials multiple contacts simultaneously.

**Steps**:
1. In Dialer Settings, select 'Predictive' mode
2. Enable/disable Auto Answer
3. Set Timeout (seconds before auto-answer)
4. Configure Timing: Ringing agent time, Wrap-up time, Max ring time
5. Set Dialing Attempts: Default retry period, Max attempts per record
6. Set Performance Metrics: Calls per agent (Auto or manual), Abandon rate %
7. Enable Answering Machine Detection
8. Configure System Disposition actions (Retry/Final per outcome)
9. Configure Agent Disposition options (which outcomes agents can select)

**Business Value**: Maximizes agent productivity for large outbound teams by minimizing idle time between calls.

---

### Preview Dialing Mode

**Module**: auto_dialer  
**Type**: configuration

Agent is shown contact details before the call is placed. Agent manually reviews and initiates the call. Best for small teams requiring manual review.

**Steps**:
1. Select 'Preview' mode in Dialer Settings

**Business Value**: Gives agents context before calling, improving conversation quality for high-value or complex contacts.

---

### Progressive Dialing Mode

**Module**: auto_dialer  
**Type**: configuration

System dials one call per available agent, maintaining steady flow. Best for small to medium teams.

**Steps**:
1. Select 'Progressive' mode in Dialer Settings

**Business Value**: Balances automation with control — no abandoned calls, steady agent workload.

---

### Agentless Dialing Mode

**Module**: auto_dialer  
**Type**: configuration

Automated outbound calling without live agents. Suitable for IVR-based campaigns, surveys, or broadcast messages.

**Steps**:
1. Select 'Agentless' mode in Dialer Settings

**Business Value**: Enables fully automated outreach at scale without requiring agent staffing.

---

### Local Presence

**Module**: auto_dialer  
**Type**: configuration

Automatically selects the best outbound business number based on the contact's area code. Makes calls appear local to the prospect, increasing answer rates.

**Steps**:
1. In General Settings, assign multiple business numbers with regional labels
2. Toggle on 'Local Presence'
3. System automatically matches caller ID to contact area code at call time

**Business Value**: Increases answer rates by displaying a local number to prospects instead of an unknown toll-free or out-of-state number.

---

### Business Hours Scheduling

**Module**: auto_dialer  
**Type**: configuration

Configure per-day calling windows for a campaign. Each day (Sunday–Saturday) can be enabled/disabled with custom AM/PM start and end times, or set to Full Day.

**Steps**:
1. In General Settings, scroll to Business Hours section
2. Enable/disable each day with checkbox
3. Set start and end times per day
4. Or toggle 'Full day' for unrestricted daily calling

**Business Value**: Ensures calls are placed only during legally and operationally acceptable hours, applied per the campaign timezone.

---

### National DNC List Scrubber

**Module**: auto_dialer  
**Type**: configuration

Upload a Do Not Call list to prevent dialing numbers on the national DNC registry. Integrated into the Campaigns screen.

**Steps**:
1. On Campaigns screen, locate 'National DNC list scrubber' panel (top right)
2. Download template if needed
3. Upload your DNC list CSV

**Business Value**: Ensures compliance with TCPA and national DNC regulations, protecting the business from legal liability.

---

### Answering Machine Detection (AMD)

**Module**: auto_dialer  
**Type**: workflow

Automatically detects when a call reaches an answering machine/voicemail. System can be configured to retry or treat as final based on AMD result.

**Steps**:
1. In Dialer Settings (Predictive mode), toggle on 'Answering machine detection'
2. In System Disposition, configure AMD outcome (Retry with period / Final)

**Business Value**: Prevents wasting agent time on voicemails and enables intelligent retry logic.

---

### System Disposition

**Module**: auto_dialer  
**Type**: configuration

Automated handling rules for call outcomes not controlled by agents (busy, no response, AMD, invalid number, robocall block). Each outcome can be set to Retry (with period and attempt limits) or Final.

**Steps**:
1. In Dialer Settings, scroll to System Disposition section
2. For each outcome (Contact busy, Contact no response, Agent abandoned, Invalid number, Answering machine, Blocked by robocall analytics): choose Retry or Final
3. For Retry: set retry period and max attempts per number

**Business Value**: Automates retry logic and eliminates manual queue management for unreachable contacts.

---

### Agent Disposition

**Module**: auto_dialer  
**Type**: configuration

Configurable set of call outcome options that agents select after each call. Each disposition can be marked as Final (removes from queue) or non-Final (remains eligible for retry). Visible options per campaign are configurable.

**Steps**:
1. In Dialer Settings, scroll to Agent Disposition section
2. Enable or disable specific disposition options for this campaign
3. Mark each as Final or not (Final = no more retries)

**Business Value**: Standardizes agent call outcomes, drives retry logic, and feeds reporting/analytics.

---

### Record List Management

**Module**: auto_dialer  
**Type**: workflow

Upload and manage contact lists (CSV format) for use in campaigns. MightyCall auto-maps CSV fields. Lists show record count, unique area codes, and coverage score.

**Steps**:
1. In campaign creation Step 4 (Record list), upload a CSV file or drag-and-drop
2. Or select an existing record list from the right panel
3. Download the template for correct CSV format
4. Note: files over 15MB take 5-7 minutes to upload
5. Review coverage score after list is attached

**Business Value**: Enables targeted outreach by attaching specific contact databases to each campaign.

---

### Coverage Score

**Module**: auto_dialer  
**Type**: report

A percentage metric showing how many unique contact area codes in the record list are covered by the campaign's assigned local business numbers. Displayed per record list and on the Campaigns list screen.

**Steps**:
1. Attach a record list to a campaign
2. Assign local business numbers in General Settings
3. Coverage Score auto-calculates and displays in the Record List step and Campaigns table

**Business Value**: Helps managers optimize local presence coverage to maximize answer rates across different geographic regions.

---

### Dialing Attempts Configuration

**Module**: auto_dialer  
**Type**: configuration

Control how many times the system retries each record and the minimum time between retries. Configured within Predictive dialer mode settings.

**Steps**:

**Business Value**: Balances contact penetration with compliance and contact experience — avoids over-dialing a single number.

---

### Campaign Analytics & Reporting

**Module**: reports  
**Type**: report

Performance dashboard for all campaigns. Shows key outbound metrics across all campaigns with filtering by date range.

**Steps**:
1. Navigate to Reports
2. Select date range filter
3. View Campaigns tab for campaign-level metrics
4. Use Columns button to show/hide metrics
5. Export data as needed

**Business Value**: Provides managers visibility into campaign performance to optimize dialer settings, abandon rates, and agent efficiency.

---

## Screens

### Campaigns List

**Purpose**: Overview of all outbound campaigns with status, agents, records, and coverage score. Entry point for campaign management.

**Components**:
- **Create campaign** (button): Opens campaign creation wizard
- **Campaigns table** (table): Lists all campaigns with Name, Description, Agents, Records, Coverage Score columns
- **Status badge** (badge): Shows Running / Ready / Completed / Paused / Incomplete per campaign
- **Play/Pause** (button): Start or pause a campaign inline
- **National DNC list scrubber** (panel): Upload DNC compliance list
- **Upload (DNC)** (button): Upload DNC CSV file
- **Download template** (link): Download DNC CSV template

---

### Campaign General Settings (Step 1)

**Purpose**: Configure campaign name, description, timezone, date range, business hours, and assigned phone numbers including local presence.

**Components**:
- **Campaign name** (input): Enter campaign title
- **Description (Optional)** (textarea): Enter campaign description, 200 char limit
- **Timezone** (dropdown): Select campaign timezone (e.g. UTC-06:00 Central Time)
- **Start date** (date_picker): Set campaign start date (optional)
- **End date** (date_picker): Set campaign end date (optional)
- **Business hours** (schedule_grid): Enable/disable each day and set AM/PM start-end times or Full Day
- **Business Numbers** (panel): Assign phone numbers to the campaign with labels (LA Main, LA Sales, NYC, Toronto, San Diego, Toll-Free)
- **Auto-rotation** (toggle): Enable number rotation
- **Local Presence** (toggle): Auto-select best number based on contact area code
- **Cancel** (button): Discard campaign and return to list
- **Save** (button): Save campaign progress

---

### Campaign Dialer Settings (Step 2)

**Purpose**: Select dialing mode (Preview, Progressive, Predictive, Agentless) and configure mode-specific parameters including timing, retry logic, AMD, and disposition options.

**Components**:
- **Dialer mode selector** (radio_group): Choose Preview / Progressive / Predictive / Agentless
- **Auto answer** (toggle): Enable automatic call pickup by agents
- **Timeout (sec)** (number_input): Seconds before auto-answer triggers
- **Ringing agent time (sec)** (number_input): How long agent phone rings
- **Wrap-up time (sec)** (number_input): Post-call wrap time before next call
- **Max ring time (sec)** (number_input): Maximum time to let contact phone ring
- **Default retry period (min)** (number_input): Minimum wait before retrying a record
- **Max attempts per record** (number_input): Maximum total dial attempts per contact
- **Calls per agent** (dropdown): Set simultaneous calls per agent (Auto or manual)
- **Abandon rate (%)** (number_input): Maximum acceptable abandoned call percentage
- **Answering machine detection** (toggle): Enable AMD
- **System disposition** (disposition_table): Set Retry/Final rules for system-level outcomes (busy, no response, AMD, invalid, blocked)
- **Agent disposition** (disposition_table): Configure which outcome options agents can select and whether each is Final

---

### Campaign Record List (Step 4)

**Purpose**: Upload a new CSV contact list or select an existing record list to use for this campaign. Shows list stats including record count, unique area codes, and coverage score.

**Components**:
- **Create record list** (dropzone): Upload or drag-and-drop CSV file
- **Upload** (button): Trigger file upload
- **Download the template** (link): Download CSV template with required field format
- **Existing record lists panel** (list): Browse and select pre-uploaded lists showing record count and unique area codes
- **New record list** (radio): Create a new list rather than reusing existing
- **Coverage Score** (column): Shows % of contact area codes covered by assigned local numbers

---

### Reports - Campaigns

**Purpose**: Analytics dashboard showing performance metrics for all outbound campaigns over a selected date range.

**Components**:
- **Date range filter** (date_filter): Filter report by date range with preset options (last 30 days, etc.)
- **Report tabs** (tabs): Switch between Campaigns / Dispositions / Agent sessions / Call details
- **Campaign metrics table** (table): Shows all campaigns with KPI columns
- **Columns** (button): Show/hide specific metric columns
- **Export** (button): Export report data

---

