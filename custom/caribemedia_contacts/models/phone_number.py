from odoo import api, models, fields

class PhoneNumber(models.Model):
    _name = 'phone.number'
    _description = 'Phone Numbers'

    partner_id = fields.Many2one('res.partner', string='Contact', ondelete='cascade', readonly=True)
    phone_number = fields.Char(string='Phone', required=True, default=lambda self:self.partner_id.phone)
    raw_phone = fields.Char(string='Raw Phone', compute='_compute_raw_phone')
    is_active = fields.Boolean(string='Active', default=True)
    is_main_phone = fields.Boolean(string='Main Phone')

    def _compute_raw_phone(self):
        for rec in self:
            rec.raw_phone = ''.join(char for char in partner_id.phone if char.isdigit())
