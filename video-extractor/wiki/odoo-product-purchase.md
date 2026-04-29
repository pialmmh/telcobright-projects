# Odoo 17 Product — Purchase Tab

Vendors that supply this product, vendor billing policy, and the chatter pane below the form.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`frame_0609`](../odoo/product/screenshots/frame_0609.jpg) · [`frame_0635`](../odoo/product/screenshots/frame_0635.jpg)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## Vendors table (top)

Backed by `product.supplierinfo`. Columns:

| Column | Notes |
|--------|-------|
| Vendor | many2one(res.partner) — e.g. `Abigail Peterson` |
| Price | monetary — e.g. `5.00` |
| Currency | many2one(res.currency) — e.g. `USD` |
| Delivery Lead Time | integer (days) |
| (Min Qty) | float — column collapses behind the settings cog at narrow widths |

Below the rows: **Add a line** link.

## VENDOR BILLS (lower-left)

| Field | Type | Notes |
|-------|------|-------|
| Vendor Taxes | many2many(account.tax) | Chip selector — e.g. `15% ×` |
| Control Policy | radio | `On ordered quantities` (control bills based on ordered qty) · `On received quantities` (control bills based on received qty) |

**Control Policy tooltip:**

> On ordered quantities: Control bills based on ordered quantities.
> On received quantities: Control bills based on received quantities.

## PURCHASE DESCRIPTION (lower-right)

Free-text area. *This note is added to purchase orders.* Carries an `EN` language indicator.

## Chatter (below the form)

| Element | Notes |
|---------|-------|
| `Send message` | purple-burgundy primary button |
| `Log note` | secondary |
| `WhatsApp` | with WhatsApp icon |
| `Activities` | scheduled activities |
| right cluster | 🔍 search · 📎 attachments · 👤1 followers count · ✓ Following toggle |

A timeline below the input shows entries like:

```
Mitchell Admin · 8 minutes ago
Model adding the necessary fields to products to use with Pricer electronic tags created
```

## See Also
- [odoo-product-modules.md](odoo-product-modules.md)
- [odoo-product-inventory.md](odoo-product-inventory.md) — procurement Routes (Buy ↔ vendors)
- [odoo-product-data-entities.md](odoo-product-data-entities.md) — `SupplierInfo`
