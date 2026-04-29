# Odoo 17 Product — General Information Tab

The default tab on the product form. Two columns: left holds product *kind* and units; right holds pricing, taxes, and categorisation.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`frame_0069`](../odoo/product/screenshots/frame_0069.jpg) · [`frame_0134`](../odoo/product/screenshots/frame_0134.jpg) · [`frame_0217`](../odoo/product/screenshots/frame_0217.jpg) · [`frame_0249`](../odoo/product/screenshots/frame_0249.jpg) · [`frame_0346`](../odoo/product/screenshots/frame_0346.jpg) · [`frame_0365`](../odoo/product/screenshots/frame_0365.jpg) · [`frame_0382`](../odoo/product/screenshots/frame_0382.jpg) · [`frame_0765`](../odoo/product/screenshots/frame_0765.jpg)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## Left column

| Field | Type | Notes |
|-------|------|-------|
| Product Type | selection | `Consumable` · `Service` · `Storable Product` · `Booking Fees` · `Combo` · `Event Ticket` · `Event Booth` · `Course` |
| Invoicing Policy | selection | `Ordered quantities` · `Delivered quantities` |
| Unit of Measure | many2one(uom.uom) | Sales UoM (e.g. Units) |
| Purchase UoM | many2one(uom.uom) | RFQ/PO UoM |
| Create Repair | boolean | Auto-create a repair order |

### Product Type tooltip text (verbatim)

> A storable product is a product for which you manage stock. The Inventory app has to be installed.
> A consumable product is a product for which stock is not managed.
> A service is a non-material product you provide.

(See [frame_0134](../odoo/product/screenshots/frame_0134.jpg).) The full dropdown also includes Booking Fees, Combo, Event Ticket, Event Booth, and Course — see [frame_0217](../odoo/product/screenshots/frame_0217.jpg).

### Below Product Type — context help (Consumable shown)

> Consumables are physical products for which you don't manage the inventory level: they are always available.
>
> You can invoice them before they are delivered.

## Right column

| Field | Type | Notes |
|-------|------|-------|
| Sales Price | monetary | Suffix `(= $X.YZ Incl. Taxes)` recomputes from Customer Taxes |
| Customer Taxes | many2many(account.tax) | Chip selector, e.g. `15% ×` |
| TaxCloud Category | many2one | TIC (Taxability Information Codes) used by TaxCloud. **Prevails over** the value set on the product category. |
| Avatax Category | many2one | Used when Avatax integration is on |
| Cost | monetary, per UoM | AVCO-computed. Used to value the product when purchase cost is unknown (e.g. inventory adjustment), and to compute margins on sale orders. |
| Product Category | many2one(product.category) | Defaults to `All`; arrow icon opens the category form |
| Part Number | text | Internal SKU |
| OEM No. | text | Manufacturer SKU |
| UPC / EAN Code | text | Barcode |
| Version | integer | Default `1` |
| Product Template Tags | many2many | Free-form tagging |
| Brands | many2one | |
| Company | many2one(res.company) | Multi-company scope |

### Cost tooltip (verbatim)

> Value of the product (automatically computed in AVCO).
> Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
> Used to compute margins on sale orders.

## Product header (always visible)

| Field | Type | Notes |
|-------|------|-------|
| Product Name | text, required | The yellow ★ icon toggles favorite |
| Image | binary | Top-right placeholder, click to upload |
| Can be Sold | boolean | |
| Can be Purchased | boolean | |
| Can be Expensed | boolean | |
| Recurring | boolean | Subscription product |
| Can be Rented | boolean | |

## See Also
- [odoo-product-modules.md](odoo-product-modules.md) — form anatomy and tab strip
- [odoo-product-variants.md](odoo-product-variants.md) — Attributes & Variants tab
- [odoo-product-data-entities.md](odoo-product-data-entities.md) — `ProductTemplate` schema
