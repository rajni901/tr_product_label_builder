from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PrintLabelWizard(models.TransientModel):
    _name = 'print.label.wizard'
    _description = 'Print Product Labels'

    template_id = fields.Many2one(
        'product.label.template',
        string='Label Template',
        required=True,
    )
    product_ids = fields.Many2many(
        'product.product',
        string='Products',
    )
    quantity = fields.Integer(string='Copies per Product', default=1, required=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        active_model = self.env.context.get('active_model')
        active_ids = self.env.context.get('active_ids', [])

        products = self.env['product.product']

        if active_model == 'product.template':
            tmpls = self.env['product.template'].browse(active_ids)
            products = tmpls.mapped('product_variant_ids')
        elif active_model == 'product.product':
            products = self.env['product.product'].browse(active_ids)
        elif active_model == 'sale.order':
            orders = self.env['sale.order'].browse(active_ids)
            products = orders.mapped('order_line.product_id')
        elif active_model == 'purchase.order':
            orders = self.env['purchase.order'].browse(active_ids)
            products = orders.mapped('order_line.product_id')
        elif active_model == 'stock.picking':
            pickings = self.env['stock.picking'].browse(active_ids)
            products = pickings.mapped('move_ids.product_id')

        if products:
            res['product_ids'] = [(6, 0, products.ids)]

        template = self.env['product.label.template'].search([], limit=1)
        if template:
            res['template_id'] = template.id

        return res

    def action_print(self):
        if not self.product_ids:
            raise UserError(_('Please select at least one product.'))
        if self.quantity <= 0:
            raise UserError(_('Copies must be greater than zero.'))

        data = {
            'template_id': self.template_id.id,
            'product_ids': self.product_ids.ids,
            'quantity': self.quantity,
            'pricelist_id': self.pricelist_id.id if self.pricelist_id else False,
        }
        return self.env.ref('tr_product_label_builder.action_report_product_label').report_action(
            self, data=data
        )
