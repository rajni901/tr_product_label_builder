from odoo import models


class ReportProductLabel(models.AbstractModel):
    _name = 'report.tr_product_label_builder.report_product_label'
    _description = 'Product Label Report'

    def _get_report_values(self, docids, data=None):
        wizards = self.env['print.label.wizard'].browse(docids)
        labels = []
        for wizard in wizards:
            for product in wizard.product_ids:
                for _ in range(wizard.quantity):
                    labels.append({
                        'product': product,
                        'template': wizard.template_id,
                        'pricelist': wizard.pricelist_id,
                    })
        return {
            'doc_ids': docids,
            'doc_model': 'print.label.wizard',
            'docs': wizards,
            'labels': labels,
            'company': self.env.company,
        }
