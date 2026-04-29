# Odoo 17 — Product Management Overview

How the **Sales > Products** module is laid out: top navigation, the Product detail form with seven tabs, smart buttons, and the Update Quantity flow. Captured from a 15-minute demo on `runbot134.odoo.com` (Sales app, Mug product).

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`../odoo/product/screenshots/`](../odoo/product/screenshots/) — 19 representative frames from a 670-scene capture

> Screenshots may be missing from a given checkout. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details from missing images.

## Top Navigation

`Sales · Orders · To Invoice · Products · Reporting · Configuration`

Right side of the top bar carries: a recording indicator, dial pad, chat (19 unread), notifications (41), tools, the active company switcher (`Beyond Sleep`), and the user avatar.

## Product detail form anatomy

```
┌─ Breadcrumb (Products / Mug)        [save dot · discard ↩]    [smart buttons row]    1/1 < > ┐
│  [New]  [Replenish] [Print Labels]                                                            │
│                                                                                               │
│  ★ Product Name (Mug)                                                  [EN]      [📷 image]  │
│  ☑ Can be Sold  ☑ Can be Purchased  ☐ Can be Expensed  ☐ Recurring  ☐ Can be Rented          │
│                                                                                               │
│  [General Information] [Attributes & Variants] [Sales] [Purchase] [Inventory] [Accounting] [eBay]
│  ─────────────────────                                                                        │
│  …two-column body…                                                                            │
│                                                                                               │
│  [Send message] [Log note] [WhatsApp] [Activities]                       🔍 📎 👤 ✓ Following │
│  …chatter…                                                                                    │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Smart-button row

| Button | Notes |
|--------|-------|
| **Extra Prices** | Pricelist rules count |
| **Documents** | Attached documents count |
| **Go to Website** | Opens public product page |
| **In: 0 / Out: 0** | Stock movement counters |
| **Variants** | Appears after Attributes & Variants is saved with values; shows variant count |
| **More ▾** | Overflow menu |

## Tabs

| Tab | Demoed | Page |
|-----|--------|------|
| General Information | yes | [`odoo-product-general.md`](odoo-product-general.md) |
| Attributes & Variants | yes | [`odoo-product-variants.md`](odoo-product-variants.md) |
| Sales | yes | [`odoo-product-sales.md`](odoo-product-sales.md) |
| Purchase | yes | [`odoo-product-purchase.md`](odoo-product-purchase.md) |
| Inventory | yes | [`odoo-product-inventory.md`](odoo-product-inventory.md) |
| Accounting | no | (visible in tab strip; not opened in this video) |
| eBay | no | (visible in tab strip; not opened in this video) |

## Update Quantity (smart-button flow)

[`odoo-product-update-quantity.md`](odoo-product-update-quantity.md) — per-variant, per-location stock grid reachable from the product form.

## Cross-module features

- Chatter pane (`Send message · Log note · WhatsApp · Activities`) at the bottom of every form.
- Field-level help tooltips (`?` superscript next to each label).
- Active-record dirty indicators (cloud-up + counter-clockwise arrow) appear in the breadcrumb area.
- Multi-language `EN` marker per text field.
- Active filter chips with `×` to dismiss in list views.

## See Also
- [odoo-product-data-entities.md](odoo-product-data-entities.md) — full entity schemas
- [odoo-product-general.md](odoo-product-general.md) — General Information tab
- [odoo-product-variants.md](odoo-product-variants.md) — attribute/variant matrix
- [AI_AGENT_GUIDE.md](AI_AGENT_GUIDE.md) — how to consume this wiki to build software
