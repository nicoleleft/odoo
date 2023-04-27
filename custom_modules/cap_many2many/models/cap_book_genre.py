from odoo import fields, api, _, models

class CapBookGenre(models.Model):
    _name = 'cap.book.genre'
    _description = 'Book Genre'

    book_ids = fields.Many2many('cap.book',string="Books")
    name = fields.Char('Description')