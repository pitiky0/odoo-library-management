from odoo import http
from odoo.http import request

class LibraryController(http.Controller):

    # 1. تعريف الرابط (Route)
    # auth='public': أي واحد يقدر يدخل (بدون يوزر ومودباس)
    # type='json': النتيجة غتكون JSON (ماشي HTML)
    # methods=['GET']: كنقبلو غير القراءة
    @http.route('/library/books', type='json', auth='public', methods=['POST'], csrf=False)
    def get_available_books(self):
        # 2. البحث عن الكتب المتوفرة
        books = request.env['library.book'].sudo().search([
            ('state', '=', 'available')
        ])
        
        # 3. تحويل البيانات لـ List of Dictionaries (JSON Format)
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'title': book.name,
                'author': book.author_id.name or 'Unknown', # تفادي الخطأ يلا ماكانش كاتب
                'year': book.year,
                'isbn': book.isbn,
            })
            
        # 4. إرجاع النتيجة
        return {
            'status': 'success',
            'total': len(book_list),
            'data': book_list
        }