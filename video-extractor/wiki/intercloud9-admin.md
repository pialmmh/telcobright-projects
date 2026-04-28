# InterCloud9 — Admin

Account-level configuration: user provisioning and custom contact field setup. URL: `/#/admin`.

**Source**: `intercloud9-dialer/knowledge_graph.json`
**Screenshots**: [`../intercloud9-dialer/screenshots/`](../intercloud9-dialer/screenshots/) — reduced set, one image per significant scene

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Account Information

Header notice on the right: `Please Logoff and Login to Enable New Settings` — reminds admins that user changes only take effect on next login.

## Users panel

Header: **Users** with `[+ Create New User]` (orange) on the right and the total count (`5 Total Users`) on the far right.

Each user row:

```
Demo 👤                                          [✏][📊][○][☎][📅][📋][🔊]
demo@intercloud9.com                             Connect via: SIP Phone
demo@intercloud9.com                             Username: sip_2  Password: 1234
+1 (212) 555-1212

Adam 👤                                          [✏][📊][○][☎][📅][📋][🔊]
adam@intercloud9.com                             Connect via: Telephone Dial-in
adam@intercloud9.com                             Agent ID: sip_155  PIN: 1234
+1 (212) 555-1212
```

### Per-user fields

| Field | Notes |
|-------|-------|
| Name | display name |
| Emails (×2) | two email fields per user (primary + alt) |
| Phone | contact phone |
| **Connect via** | `SIP Phone` *or* `Telephone Dial-in` — determines the credential pair below |
| Username + Password | shown when Connect via = SIP Phone (e.g. `sip_2 / 1234`) |
| Agent ID + PIN | shown when Connect via = Telephone Dial-in (e.g. `sip_155 / 1234`) |

> **Note**: Passwords/PINs are displayed in plaintext to admins.

### Per-user action icons

| Icon | Action (tooltip seen when available) |
|------|--------------------------------------|
| ✏️ | Edit user |
| 📊 | Stats — agent productivity |
| ⊙ | Status / activity |
| ☎ | Phone setup |
| 📅 | Calendar / schedule |
| 📋 | Log |
| 🔊 | **Recordings (Direct Calls Only)** — tooltip explicitly noted; campaign call recordings live elsewhere |

## Setup Database Fields

Bottom-right link: **Setup Database Fields** — opens the configurator for custom Contact fields. The Contact View `Lead ID` row shows greyed text *"Change or add fields"*, which is where these get rendered. Detail not captured in this video.

## See Also
- [intercloud9-data-entities.md](intercloud9-data-entities.md) — User entity (SIP vs Dial-in fields)
- [intercloud9-agent-monitor.md](intercloud9-agent-monitor.md) — uses provisioned users for live monitoring + barge
- [intercloud9-contact-view.md](intercloud9-contact-view.md) — where Setup Database Fields shows up to agents
