from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a One2many field for multiple phone numbers
    phone_ids = fields.One2many('phone.number', 'partner_id', string='Additional Phones')


