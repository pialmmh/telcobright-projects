# Odoo 17 Product — Update Quantity

Per-variant, per-location on-hand grid. Reached from the smart-button row of the product form. URL pattern: `Products / <Mug> / Update Quantity`.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`frame_0806`](../odoo/product/screenshots/frame_0806.jpg) · [`frame_0838`](../odoo/product/screenshots/frame_0838.jpg)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## Layout

```
[ New ]  [ Inventory at Date ]   Products / Mug / Update Quantity ⚙
                                 🔍  ▼ Internal Locations ×   ▼ On Hand ×   Search…    1-2/2  < >    ☰ ⊞ 📊
```

| Column | Type | Notes |
|--------|------|-------|
| Location | many2one(stock.location) | e.g. `WH/Stock` |
| Product | many2one(product.product) | Variant — link to variant detail |
| Owner | many2one(res.partner) | Optional — e.g. `Abigail Peterson` |
| On Hand Quantity | float, editable | Inline pencil ✎ icon for edit-in-place |
| Reserved | float, read-only | Reserved by outgoing transfers |
| Unit | text | Display of the variant's UoM |
| (right column) | actions | `↺ History` · `🔄 Replenishment` (and `📊 Valuation` when applicable) |

A totals row at the bottom sums the numeric columns:

```
                                10.00      0.00
```

## Empty-state

When no quants exist:

> 📁 **No Stock On Hand**
>
> This analysis gives you an overview of the current stock level of your products.

(Placeholder rows are rendered behind the empty-state graphic with greyed-out lorem-ipsum-like content.)

## View toggles (top-right)

`☰ list · ⊞ kanban · 📊 graph` — standard Odoo trio. The active filters `Internal Locations` and `On Hand` are pre-applied for this entry point.

## Header buttons

| Button | Effect |
|--------|--------|
| **New** | Create a new stock quant row inline |
| **Inventory at Date** | Switch the grid to a point-in-time stock snapshot |

## See Also
- [odoo-product-inventory.md](odoo-product-inventory.md) — procurement Routes that drive replenishment
- [odoo-product-variants.md](odoo-product-variants.md) — variants are the rows of this grid
- [odoo-product-data-entities.md](odoo-product-data-entities.md) — `StockQuant`
