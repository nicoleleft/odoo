from odoo import fields, api, models, _

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    purchase_ids = fields.Many2many('purchase.order',string="Purchase Orders")