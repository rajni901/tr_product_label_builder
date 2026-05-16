{
    'name': 'Product Label Builder Pro',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Products',
    'summary': 'Design and print professional product labels with custom templates, barcode, QR, logo and more',
    'description': """
Product Label Builder Pro — by Technical Rajni
===============================================
Design beautiful product labels and print them in bulk.

Features:
- Multiple label templates (size, fields, colors)
- Print from Product, Sale Order, Purchase Order, Inventory
- Fields: Name, SKU, Price, Barcode, QR Code, Lot, Expiry, Company Logo
- Custom label sizes (A4, 50x30mm, 100x50mm, Dymo, custom)
- Bulk print wizard with quantity control
- Professional PDF output
    """,
    'author': 'Technical Rajni',
    'website': 'https://www.technicalrajni.com',
    'license': 'OPL-1',
    'depends': ['product', 'stock', 'sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'report/label_report.xml',
        'views/label_template_views.xml',
        'wizard/print_label_wizard_views.xml',
        'views/product_views.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'tr_product_label_builder/static/src/css/label_style.css',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 19.00,
    'currency': 'USD',
}
