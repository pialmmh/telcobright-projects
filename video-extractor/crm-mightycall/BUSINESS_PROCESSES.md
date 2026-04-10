# MightyCall Predictive Dialer Business Processes

## Process Diagrams

### Outbound Predictive Dialing Campaign

End-to-end business process for running a predictive dialing outbound sales or outreach campaign.

**Actors**: Campaign Manager, Sales Agent, System (Auto Dialer)

**Triggers**: New sales campaign initiated, New contact list available, Scheduled campaign start date reached

**Process Steps**:

```
  □ Create campaign with general settings (Campaign Manager)
  □ Configure predictive dialer mode and parameters (Campaign Manager)
  □ Upload contact record list (CSV) (Campaign Manager)
  □ Validate coverage score for local presence (Campaign Manager)
  ○ System begins auto-dialing contacts
  ◇ Contact answers — system connects to available agent (System)
  □ Agent conducts call (Sales Agent)
  □ Agent selects disposition outcome (Sales Agent)
  ◇ System applies retry/final logic based on disposition (System)
  □ System retries or removes record from queue (System)
  □ Manager reviews campaign analytics in Reports (Campaign Manager)
```

**Outcomes**: Successful contacts made, Appointments booked, Leads qualified, Campaign completed with performance report

---

### DNC Compliance Management

Process for ensuring outbound calls comply with Do Not Call regulations.

**Actors**: Compliance Manager

**Triggers**: Before campaign launch, DNC list updated

**Process Steps**:

```
  □ Download DNC list template (Compliance Manager)
  □ Upload National DNC list to MightyCall (Compliance Manager)
  □ System scrubs campaign record lists against DNC (System)
```

**Outcomes**: DNC-compliant record list, Reduced regulatory risk

---

