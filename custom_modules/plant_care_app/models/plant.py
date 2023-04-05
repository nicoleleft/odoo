from odoo import models, fields

class Plants(models.Model):
    _name = 'plant'
    _description = 'Plant'

    name = fields.Char(string = "Plant name", required=True)
    watering_schedule = fields.Integer("Watering Schedule", required=True)
    time_unit = fields.Selection([('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], required=True)
    image = fields.Binary("Photo of Plant")