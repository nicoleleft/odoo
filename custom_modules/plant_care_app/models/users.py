import csv
from odoo import models, fields, api

class Users(models.Model):
    _name = 'users'
    _description = 'Users record'

    name = fields.Char(string = "Name")
    id = fields.Integer(string = "User ID")
    plants = fields.Char(string="Plants")

    #   Helper function to display list of plants?
    @api.model
    def create_demo_data(self):
        with open('/data/plant_parents.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.env['users'].create({
                    'name': row['name'],
                    'id': row['id'],
                    'plants': row['plants']
                })
