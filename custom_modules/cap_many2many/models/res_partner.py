from odoo import fields, _, api, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    characteristic_ids = fields.Many2many('res.partner.characteristics',string="Characteristics")