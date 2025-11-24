from odoo import models, fields, tools

class LibraryBookStatistics(models.Model):
    _name = 'library.book.statistics'
    _description = 'Library Book Statistics'
    _auto = False # ⚠️ مهمة جداً: كتقول لـ Odoo ما يصاوبش الجدول
    
    # الحقول اللي غتكون فالتقرير
    author_id = fields.Many2one('library.author', string='Author', readonly=True)
    book_count = fields.Integer(string='Book Count', readonly=True)
    average_rating = fields.Float(string='Average Rating', readonly=True)

    def init(self):
        # هنا كنمسحو الـ View القديمة يلا كانت، وكنعاودو نبنيوها
        tools.drop_view_if_exists(self.env.cr, self._name.replace(".", "_"))
        
        # كنزرعو الـ SQL Query
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW library_book_statistics AS (
                SELECT
                    min(b.id) as id,  -- ضروري Odoo يحتاج ID فريد
                    b.author_id,
                    count(b.id) as book_count,
                    avg(b.rating) as average_rating
                FROM
                    library_book b
                WHERE
                    b.author_id IS NOT NULL
                GROUP BY
                    b.author_id
            )
        """)