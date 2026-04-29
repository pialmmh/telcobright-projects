# Odoo 17 Product — Inventory Tab

Procurement routes, logistics metadata for shipping/customs, and three per-document description fields.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`frame_0668`](../odoo/product/screenshots/frame_0668.jpg) · [`frame_0678`](../odoo/product/screenshots/frame_0678.jpg)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## OPERATIONS (left column)

### Routes (multi-checkbox)

| Route | Notes |
|-------|-------|
| Dropship Subcontractor on Order | |
| Buy | Default checked when "Can be Purchased" is on |
| Replenish on Order (MTO) | Make-to-order |
| Manufacture | Requires Manufacturing app |
| Resupply Subcontractor on Order | |
| Dropship | |
| `<Company>: Cross-Dock` | e.g. `YourCompany: Cross-Dock` — appears once cross-dock is configured at company level |

Below the checkboxes: **→ View Diagram** link (renders the procurement chain visually).

## LOGISTICS (right column)

| Field | Type | Notes |
|-------|------|-------|
| Responsible | many2one(res.users) | Default Mitchell Admin in demo |
| Customer Lead Time | float (days) | Default `0` |
| HS Code | text | *Standardized code for international shipping and goods declaration. At the moment, only used for the FedEx shipping provider.* |
| Origin of Goods | many2one(res.country) | *Rules of origin determine where goods originate, i.e. not where they have been shipped from, but where they have been produced or manufactured. As such, the 'origin' is the 'economic nationality' of goods traded in commerce.* |

## Per-document descriptions (full width, stacked)

Each is a free-text area with an `EN` language marker.

| Section | Description hint |
|---------|------------------|
| DESCRIPTION FOR RECEIPTS | *This note is added to receipt orders (e.g. where to store the product in the warehouse).* |
| DESCRIPTION FOR DELIVERY ORDERS | *This note is added to delivery orders.* |
| DESCRIPTION FOR INTERNAL TRANSFERS | (free text) |

## See Also
- [odoo-product-modules.md](odoo-product-modules.md)
- [odoo-product-update-quantity.md](odoo-product-update-quantity.md) — actual on-hand stock
- [odoo-product-purchase.md](odoo-product-purchase.md) — Buy route + vendors
- [odoo-product-data-entities.md](odoo-product-data-entities.md)
