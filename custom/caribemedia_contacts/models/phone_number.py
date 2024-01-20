from odoo import models, fields

class PhoneNumber(models.Model):
    _name = 'phone.number'
    _description = 'Phone Numbers'

    partner_id = fields.Many2one('res.partner', string='Contact', ondelete='cascade', readonly=True, store=True)
    phone_number = fields.Char(string='Phone', required=True, default=lambda self:self.partner_id.phone, store=True)
    raw_phone = fields.Char(string='Raw Phone', compute='_compute_raw_phone', store=True)
    is_active = fields.Boolean(string='Active', default=True, store=True)
    is_main_phone = fields.Boolean(string='Main Phone', store=True)

    def _compute_raw_phone(self):
        for rec in self:
            rec.raw_phone = ''.join(char for char in partner_id.phone if char.isdigit())
