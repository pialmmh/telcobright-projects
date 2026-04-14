# Salesforce Sales Cloud — Data Entities

All entities, fields, and relationships observed in the tutorial video.

**Source**: `salesforce-crm/knowledge_graph.json`

## Entity Relationships

```
Lead ──converts to──▶ Account + Contact + Opportunity
Account ──has many──▶ Contact
Account ──has many──▶ Opportunity
Account ──has many──▶ Case
Contact ──has many──▶ Case
Contact ──belongs to──▶ Account
Contact ──reports to──▶ Contact (hierarchy)
Opportunity ──belongs to──▶ Account
Opportunity ──linked to──▶ Campaign (Primary Campaign Source)
Case ──belongs to──▶ Contact
Case ──belongs to──▶ Account
Campaign ──has many──▶ Lead (Campaign Members)
Campaign ──has many──▶ Contact (Campaign Members)
Campaign ──has many──▶ Opportunity (via Primary Campaign Source)
Task ──assigned to──▶ User
Task ──related to──▶ any record
Event ──assigned to──▶ User
Event ──related to──▶ any record
Report ──belongs to──▶ Folder
Dashboard ──belongs to──▶ Folder
Dashboard widget ──source──▶ Report
```

## Lead

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| salutation | Enum | Mr., Ms., Dr., etc. |
| first_name | String | |
| last_name | String | Required |
| company | String | Required |
| title | String | |
| phone | String | |
| mobile | String | |
| email | Email | |
| website | URL | |
| lead_status | Enum | New, Working, Unqualified, Converted |
| rating | Enum | Hot, Warm, Cold |
| lead_source | Enum | Advertisement, Employee Referral, External Referral, In-Store, On Site, Other, Social, Trade Show, Web, Word of mouth |
| follow_up | Boolean | |
| address | String | |
| city | String | |
| state | String | |
| zip | String | |
| country | String | |
| num_employees | Integer | |
| annual_revenue | Currency | |
| industry | Enum | |
| description | Text | |
| owner | Reference | User |
| converted | Boolean | |
| converted_account | Reference | Account |
| converted_contact | Reference | Contact |
| converted_opportunity | Reference | Opportunity |
| created_date | DateTime | |

## Account

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| account_name | String | Required |
| phone | String | |
| fax | String | |
| website | URL | |
| type | Enum | Prospect, Partner, Customer, Reseller |
| industry | Enum | |
| employees | Integer | |
| annual_revenue | Currency | |
| description | Text | |
| parent_account | Reference | Account (hierarchy) |
| billing_street | String | |
| billing_city | String | |
| billing_state | String | |
| billing_zip | String | |
| billing_country | String | |
| shipping_street | String | |
| shipping_city | String | |
| shipping_state | String | |
| shipping_zip | String | |
| shipping_country | String | |
| owner | Reference | User |

## Contact

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| salutation | Enum | |
| first_name | String | |
| last_name | String | Required |
| account_name | Reference | Account (Required) |
| title | String | |
| phone | String | |
| mobile | String | |
| email | Email | |
| reports_to | Reference | Contact (hierarchy) |
| lead_source | Enum | Same as Lead |
| fax | String | |
| department | String | |
| home_phone | String | |
| mailing_street | String | |
| mailing_city | String | |
| mailing_state | String | |
| mailing_zip | String | |
| mailing_country | String | |
| other_street | String | |
| other_city | String | |
| other_state | String | |
| other_zip | String | |
| other_country | String | |
| owner | Reference | User |

## Opportunity

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| opportunity_name | String | Required |
| account_name | Reference | Account |
| close_date | Date | Required |
| stage | Enum | Qualification, Proposal/Price Quote, Negotiation/Review, Closed Won, Closed Lost |
| amount | Currency | |
| probability | Integer | % — auto-set by Stage |
| type | Enum | New Business, Existing Business |
| lead_source | Enum | |
| next_step | String | |
| description | Text | |
| follow_up | Boolean | |
| primary_campaign_source | Reference | Campaign |
| owner | Reference | User |
| created_date | DateTime | |

## Case

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| case_number | String | Auto-generated (e.g. 00001031) |
| subject | String | Required |
| status | Enum | New, Open, Pending, Escalated, Closed |
| priority | Enum | Critical, High, Medium, Low |
| type | Enum | Problem, Question, Feature Request |
| case_origin | Enum | Facebook, Twitter, Email, Web, Phone |
| case_reason | Enum | New problem, Instructions not clear, User didn't attend training |
| description | Text | |
| internal_comments | Text | Not visible to customer |
| web_email | Email | |
| contact | Reference | Contact |
| account | Reference | Account |
| owner | Reference | User |
| date_time_opened | DateTime | |

## Task

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| subject | String | Required |
| status | Enum | Not Started, In Progress, Completed |
| priority | Enum | Normal, High, Low |
| due_date | Date | |
| comments | Text | |
| reminder_set | Boolean | |
| reminder_date | DateTime | |
| assigned_to | Reference | User |
| related_to | Polymorphic | Any record |
| name | Reference | Contact or Lead |

## Event

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| subject | String | Required |
| all_day_event | Boolean | |
| private | Boolean | |
| start_date | Date | |
| start_time | Time | |
| end_date | Date | |
| end_time | Time | |
| location | String | |
| show_time_as | Enum | Busy, Free |
| description | Text | |
| assigned_to | Reference | User |
| related_to | Polymorphic | Any record |

## Campaign

| Field | Type | Notes |
|-------|------|-------|
| id | Auto | |
| campaign_name | String | Required |
| status | Enum | Planned, Active, Aborted, Completed |
| type | Enum | Referral Program, Email, Webinar, Conference, Direct Mail, Advertisement |
| active | Boolean | |
| parent_campaign | Reference | Campaign (hierarchy) |
| description | Text | |
| start_date | Date | |
| end_date | Date | |
| num_sent | Integer | |
| expected_response_pct | Decimal | |
| expected_revenue | Currency | |
| budgeted_cost | Currency | |
| actual_cost | Currency | |
| responses_in_campaign | Integer | |
| owner | Reference | User |

## Report

| Field | Type |
|-------|------|
| report_name | String |
| description | Text |
| folder | Reference |
| type | Enum (Tabular, Summary, Matrix, Joined) |
| created_by | Reference (User) |
| created_on | DateTime |
| subscribed | Boolean |

## Dashboard

| Field | Type |
|-------|------|
| dashboard_name | String |
| description | Text |
| folder | Reference |
| created_by | Reference (User) |
| created_on | DateTime |
| subscribed | Boolean |
| widgets | Widget[] |
