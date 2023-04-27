from odoo import models, fields, _, api

class ResPartnerCharacteristics(models.Model):
    _name = 'res.partner.characteristics'
    _description = 'Characteristics'

    partner_ids = fields.Many2many('res.partner',string="Partners")