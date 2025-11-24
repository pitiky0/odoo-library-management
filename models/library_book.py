from odoo import models, fields, api
import logging

# هادي باش نقدرو نكتبو في الـ Log ديال السيرفر
_logger = logging.getLogger(__name__)

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    year = fields.Integer(string='Year')
    isbn = fields.Char(string='ISBN')
    numberOfPages = fields.Integer(string='Number of Pages')
    genre = fields.Char(string='Genre')
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented')
    ], string='State', default='available')

    # 👇 الحقل الجديد
    rating = fields.Integer(string='Rating', default=0)
    
    author_id = fields.Many2one('library.author', string='Author')
    
    # 👇 1. زدنا هاد الحقل باش نسجلو فوقاش خاصو يرجع
    date_return = fields.Date(string='Date to Return')

    # 👇 2. هادي هي الدالة اللي غيعيط عليها الـ Cron
    @api.model
    def check_overdue_books(self):
        # قلب على الكتب المسلفة + التاريخ ديال الارجاع صغر من اليوم
        overdue_books = self.search([
            ('state', '=', 'rented'),
            ('date_return', '<', fields.Date.today())
        ])
        
        for book in overdue_books:
            # في الحقيقة، هنا خاصنا نصيفطو Email
            # دابا غنديرو غير Log باش نشوفوه فالترمينال
            _logger.info('⚠️ Overdue Book Found: %s (Due: %s)', book.name, book.date_return)