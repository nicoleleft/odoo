from odoo import models, fields

class Plants(models.Model):
    _name = 'plant'

    name = fields.Char(string = "Plant name")
    watering_schedule = fields.Integer()
    time_unit = fields.Selection([('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')])