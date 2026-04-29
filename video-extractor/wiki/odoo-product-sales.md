# Odoo 17 Product — Sales Tab

Cross-sell suggestions, POS visibility, eCommerce surfacing, Self-Order/Kiosk description, and extra media.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`frame_0499`](../odoo/product/screenshots/frame_0499.jpg) · [`frame_0594`](../odoo/product/screenshots/frame_0594.jpg)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## Sections (two-column layout)

### UPSELL & CROSS-SELL (left)

| Field | Type | Helper text on form |
|-------|------|---------------------|
| Optional Products | many2many(product.template) | *Recommend when 'Adding to Cart' or quotation* |
| Accessory Products | many2many(product.template) | *Suggested accessories in the eCommerce cart* |
| Alternative Products | many2many(product.template) | *Displayed in bottom of product pages* |

**Optional Products tooltip:**

> Optional Products are suggested whenever the customer hits *Add to Cart* (cross-sell strategy, e.g. for computers: warranty, software, etc.).

### POINT OF SALE (left, lower)

| Field | Type | Notes |
|-------|------|-------|
| Available in POS | boolean | |
| To Weigh With Scale | boolean | |
| Category | many2one(pos.category) | Chip selector — example value `Drinks ×` |
| Available in Self Order | boolean | |

### PRODUCT DESCRIPTION FOR SELF ORDER (right, top)

Free-text area. Placeholder: *Information about your product for Self Order and Kiosk*.

### ECOMMERCE SHOP (right, lower)

| Field | Type | Notes |
|-------|------|-------|
| Website | many2one(website) | e.g. `My Website` |
| Categories | many2many(product.public.category) | Chip selector — example `Furnitures ×` |

### EXTRA PRODUCT MEDIA (bottom)

A button **Add a Media** to attach images/videos beyond the main product image.

## See Also
- [odoo-product-modules.md](odoo-product-modules.md)
- [odoo-product-purchase.md](odoo-product-purchase.md) — vendor-side counterparts
- [odoo-product-data-entities.md](odoo-product-data-entities.md) — `ProductTemplate` Sales-tab fields
