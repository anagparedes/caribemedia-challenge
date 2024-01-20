from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    call_id = fields.Char(string='Call ID')
    sale_type = fields.Selection([
        ('recorded', 'Recorded'),
        ('signed', 'Signed'),
    ], string='Sale Type')