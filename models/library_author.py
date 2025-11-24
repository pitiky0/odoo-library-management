from odoo import models, fields, api

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Name', required=True)
    
    # العلاقة العكسية مع الكتب
    book_ids = fields.One2many(
        comodel_name='library.book', 
        inverse_name='author_id', 
        string='Books'
    )
    
    # الحقل المحسوب
    book_count = fields.Integer(string='Book Count', compute='_compute_book_count')

    @api.depends('book_ids')
    def _compute_book_count(self):
        for r in self:
            r.book_count = len(r.book_ids)