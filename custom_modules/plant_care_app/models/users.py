import csv
from odoo import models, fields, api

class Users(models.Model):
    _name = 'users'
    _description = 'Users record'

    name = fields.Many2one("res.users", string = "Name")
    id = fields.Integer(string = "User ID")
    plants = fields.Char(string="Plants")

