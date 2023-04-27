from odoo import fields, models, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    warehouse_ids = fields.Many2many('stock.warehouse',string="Warehouses")