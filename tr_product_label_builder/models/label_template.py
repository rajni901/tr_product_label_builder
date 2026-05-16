from odoo import fields, models


class ProductLabelTemplate(models.Model):
    _name = 'product.label.template'
    _description = 'Product Label Template'
    _rec_name = 'name'

    name = fields.Char(string='Template Name', required=True)
    active = fields.Boolean(default=True)

    # Label Size
    label_size = fields.Selection([
        ('50x30', '50 x 30 mm (Small)'),
        ('100x50', '100 x 50 mm (Medium)'),
        ('100x70', '100 x 70 mm (Large)'),
        ('dymo', 'Dymo 89 x 28 mm'),
        ('a4', 'A4 Sheet (3 x 8 grid)'),
    ], string='Label Size', default='100x50', required=True)

    # Fields to show
    show_name = fields.Boolean(string='Product Name', default=True)
    show_internal_ref = fields.Boolean(string='Internal Reference', default=True)
    show_barcode = fields.Boolean(string='Barcode', default=True)
    show_qr_code = fields.Boolean(string='QR Code', default=False)
    show_price = fields.Boolean(string='Sale Price', default=True)
    show_category = fields.Boolean(string='Category', default=False)
    show_logo = fields.Boolean(string='Company Logo', default=True)
    show_lot = fields.Boolean(string='Lot / Serial Number', default=False)

    # Styling
    header_color = fields.Char(string='Header Color', default='#1a1a5e')
    text_color = fields.Char(string='Text Color', default='#2d2d2d')
    font_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], string='Font Size', default='medium')

    notes = fields.Char(string='Footer Note', help='e.g. www.yourstore.com')
