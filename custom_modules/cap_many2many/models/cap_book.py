from odoo import fields, models, _, api

class CapBooks(models.Model):
    _name = 'cap.book'
    _description = 'Book'

    genre_ids = fields.Many2many('cap.book.genre',string="Genres")
    name = fields.Char('Description')