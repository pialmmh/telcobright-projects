# Odoo 17 Product — Attributes & Variants Tab

Configure variant attributes (e.g. `Color: White / Black / Green / Pink`). After saving, Odoo materialises the cartesian product as `product.product` records and surfaces a **Variants** smart button on the form.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`frame_0422`](../odoo/product/screenshots/frame_0422.jpg) · [`frame_0427`](../odoo/product/screenshots/frame_0427.jpg) · [`frame_0447`](../odoo/product/screenshots/frame_0447.jpg)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## Layout

Two-column table:

| Attribute | Values |
|-----------|--------|
| Color | `White ×`  `Black ×`  `Green ×`  `Pink ×`  ▾ |

- Each value is a coloured chip. The chip background follows the value's display colour (`White` shows on green-tinted demo, `Black` on red-tinted, `Pink` on light pink — the colour is per-value metadata, not strictly the colour name).
- The dropdown to add another value lists existing values (`Dark Blue · Grey · Blue · Pink · Yellow · Rainbow`) with `Search More…` and `Start typing…` rows at the bottom.
- Right of the row: **Configure** button + 🗑 trash icon. A drag handle on the very left of the row reorders attribute lines.
- **Add a line** link below the table adds another attribute row.

## Inline warning

> **Warning**: adding or deleting attributes will delete and recreate existing variants and lead to the loss of their possible customizations.

## Sales Variant Selection (radio, below the warning)

| Option | Meaning |
|--------|---------|
| Product Configurator | Step-through dialog when adding the product to a sale order |
| Order Grid Entry | Matrix entry on the sale order line |

## Behaviour after save

The breadcrumb area shows save (cloud-up) and discard (counter-clockwise arrow) icons while the record is dirty. After save, the smart-button row gains:

```
🌐 Variants
   4
```

(See [frame_0447](../odoo/product/screenshots/frame_0447.jpg).) The number is the count of generated `product.product` records.

## See Also
- [odoo-product-modules.md](odoo-product-modules.md) — smart-button row including Variants
- [odoo-product-update-quantity.md](odoo-product-update-quantity.md) — variants appear as separate rows in the stock grid
- [odoo-product-data-entities.md](odoo-product-data-entities.md) — `AttributeLine`, `ProductAttribute`, `ProductAttributeValue`, `ProductProduct`
