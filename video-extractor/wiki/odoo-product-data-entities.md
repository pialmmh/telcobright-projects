# Odoo 17 Product — Data Entities

All entity fields and relationships visible in the demo. Use this for DB design when cloning the Sales > Products module. Field names follow Odoo's `product.*` / `stock.*` conventions; the `table_hint` lines map them to Odoo model names.

**Source**: `odoo/product/knowledge_graph.json`
**Screenshots**: [`../odoo/product/screenshots/`](../odoo/product/screenshots/)

> Screenshots may be missing. Wiki text + `knowledge_graph.json` are authoritative; do not fabricate visual details.

## Entity Relationship Overview

```
ProductTemplate (product.template)
  ├── has many → AttributeLine
  │                ├── belongs to → ProductAttribute
  │                └── has many   → ProductAttributeValue
  ├── has many → ProductProduct (variants)
  │                └── has many → StockQuant
  ├── has many → SupplierInfo (vendor pricelist)
  ├── belongs to → ProductCategory
  ├── many2many → ProductTemplateTag
  └── many2many → public.category, optional/accessory/alternative ProductTemplate
```

## ProductTemplate — `product.template`

The main editable record.

### Header

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| name | text | required |
| image | binary | |
| is_favorite | boolean | yellow ★ in header |
| can_be_sold | boolean | |
| can_be_purchased | boolean | |
| can_be_expensed | boolean | |
| recurring | boolean | subscription product |
| can_be_rented | boolean | |

### General Information

| Field | Type | Notes |
|-------|------|-------|
| product_type | selection | `Consumable` · `Service` · `Storable Product` · `Booking Fees` · `Combo` · `Event Ticket` · `Event Booth` · `Course` |
| invoicing_policy | selection | `Ordered quantities` · `Delivered quantities` |
| uom_id | many2one(uom.uom) | Sales UoM |
| uom_po_id | many2one(uom.uom) | Purchase UoM |
| create_repair | boolean | |
| list_price | monetary | Sales Price |
| taxes_id | many2many(account.tax) | Customer Taxes |
| tic_category_id | many2one | TaxCloud TIC |
| avatax_category_id | many2one | |
| standard_price | monetary | Cost (AVCO) |
| categ_id | many2one(product.category) | default `All` |
| default_code | text | Part Number |
| oem_no | text | |
| barcode | text | UPC / EAN |
| version | integer | default `1` |
| product_template_tag_ids | many2many(product.template.tag) | |
| brand_id | many2one | |
| company_id | many2one(res.company) | multi-company scope |

### Sales tab

| Field | Type | Notes |
|-------|------|-------|
| optional_product_ids | many2many(product.template) | shown on Add-to-Cart |
| accessory_product_ids | many2many(product.template) | eCommerce cart accessories |
| alternative_product_ids | many2many(product.template) | bottom of product page |
| available_in_pos | boolean | |
| to_weight | boolean | To Weigh With Scale |
| pos_categ_id | many2one(pos.category) | e.g. Drinks |
| available_in_self_order | boolean | |
| self_order_description | text | Self Order / Kiosk |
| website_id | many2one(website) | |
| public_categ_ids | many2many(product.public.category) | eCommerce categories |
| media_ids | one2many | Extra Product Media |
| sales_variant_selection | selection | `Product Configurator` · `Order Grid Entry` |

### Purchase tab

| Field | Type | Notes |
|-------|------|-------|
| seller_ids | one2many(product.supplierinfo) | Vendors table |
| supplier_taxes_id | many2many(account.tax) | Vendor Taxes |
| purchase_method | selection | `On ordered quantities` · `On received quantities` |
| description_purchase | text | Note added to purchase orders |

### Inventory tab

| Field | Type | Notes |
|-------|------|-------|
| route_ids | many2many(stock.route) | Buy / MTO / Manufacture / Dropship / Cross-Dock / Resupply / Dropship-Sub |
| responsible_id | many2one(res.users) | |
| sale_delay | float (days) | Customer Lead Time |
| hs_code | text | International shipping (FedEx) |
| country_of_origin | many2one(res.country) | Rules of origin |
| description_pickingin | text | Receipts |
| description_pickingout | text | Delivery orders |
| description_picking | text | Internal transfers |

## AttributeLine — `product.template.attribute.line`

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| product_tmpl_id | many2one(product.template) | |
| attribute_id | many2one(product.attribute) | e.g. Color |
| value_ids | many2many(product.attribute.value) | e.g. White, Black, Green, Pink |

## ProductAttribute — `product.attribute`

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| name | text | e.g. Color |
| display_type | selection | `radio` · `select` · `color` (chip background colour visible in demo) |

## ProductAttributeValue — `product.attribute.value`

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| attribute_id | many2one(product.attribute) | |
| name | text | White, Black, Green, Pink, Dark Blue, Grey, Blue, Yellow, Rainbow |
| html_color | text | drives the chip background |

## ProductProduct — `product.product`

The materialised variant. One per cartesian combination of selected attribute values.

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| product_tmpl_id | many2one(product.template) | |
| combination | many2many(product.attribute.value) | distinct combination |
| default_code | text | variant SKU override |
| barcode | text | variant barcode override |

## SupplierInfo — `product.supplierinfo`

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| product_tmpl_id | many2one(product.template) | |
| partner_id | many2one(res.partner) | Vendor |
| price | monetary | |
| currency_id | many2one(res.currency) | |
| delay | integer | Delivery Lead Time |
| min_qty | float | Min. Quantity |

## StockQuant — `stock.quant`

Backs the Update Quantity grid.

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| product_id | many2one(product.product) | variant |
| location_id | many2one(stock.location) | e.g. `WH/Stock` |
| owner_id | many2one(res.partner) | optional |
| quantity | float | On Hand Quantity (editable) |
| reserved_quantity | float | read-only |
| uom_id | many2one(uom.uom) | |

## ProductCategory — `product.category`

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| name | text | seed: `All` |
| parent_id | many2one(product.category) | |

## ProductTemplateTag — `product.template.tag`

| Field | Type | Notes |
|-------|------|-------|
| id | uuid | |
| name | text | |

## See Also
- [odoo-product-modules.md](odoo-product-modules.md) — module overview
- [odoo-product-general.md](odoo-product-general.md) — General Information field detail
- [odoo-product-variants.md](odoo-product-variants.md) — attribute matrix UX
- [odoo-product-update-quantity.md](odoo-product-update-quantity.md) — `StockQuant` UX
