# InterCloud9 — Agent Monitor

Live supervisor view of all agents currently logged in. URL: `/#/monitor`.

**Source**: `intercloud9-dialer/knowledge_graph.json` (frames 0227, 0268)
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Tabs

| Tab | Purpose |
|-----|---------|
| **Real-Time Monitor** | Live agent status table with barge controls |
| **Recorded Calls** | Browse and play back past call recordings |

## Real-Time Monitor tab

Two-pane layout. Left: outgoing call counter. Right: agent status table.

```
Real-Time Monitor | Recorded Calls
┌──────────────────┬───────────────────────────────────────────┐
│ Outgoing Calls   │ Name    Campaign  Status     Time         │
│ (0 total)        │ Adam    unkn      Unknown    unkn    🔊   │
│                  │ Alex    unkn      Unknown    unkn    🔊   │
│                  │ Demo    unkn      Unknown    unkn    🔊   │
│                  │ Greg    unkn      Unknown    unkn    🔊   │
│                  │ Jason   unkn      Unknown    unkn    🔊   │
└──────────────────┴───────────────────────────────────────────┘

⚠ Press the Speech Balloon Button Next to an Agent to Barge (Listen) In.
   A SIP connection is required.
   On a call, press '2' to coach your agent, press '1' to speak with their
   contact, or press '3' to conference.
```

### Agent status table

| Column | Notes |
|--------|-------|
| Name | Agent display name (link to detail) |
| Campaign | Active campaign, or `unkn` if idle |
| Status | `Available · On Call · Wrap-up · Unknown` |
| Time | Time in current state |
| 🔊 | Barge / Listen button (per row) |

### Barge / coaching modes

The supervisor must already be on an inbound SIP call to use barge. Once connected, DTMF keypresses control the role:

| Key | Mode | Who hears the supervisor |
|-----|------|--------------------------|
| **2** | Coach (whisper) | Only the agent |
| **1** | Takeover | Only the contact |
| **3** | Conference | Both agent + contact |

This is the **whisper / barge / conference** triad that's standard in contact centres — the same model that MightyCall calls *coach / barge / 3-way*.

## Recorded Calls tab

Listed but the table contents weren't captured in this video segment. Implied schema: time, agent, contact, duration, recording playback.

## See Also
- [intercloud9-admin.md](intercloud9-admin.md) — agent provisioning (User entity, SIP credentials)
- [intercloud9-data-entities.md](intercloud9-data-entities.md) — User, CallRecord, Recording schemas
- [intercloud9-contact-view.md](intercloud9-contact-view.md) — what the agent sees on their side
