from odoo import models, fields, api

class LibraryRentWizard(models.TransientModel):
    _name = 'library.rent.wizard'
    _description = 'Rent Book Wizard'

    book_id = fields.Many2one('library.book', string='Book', required=True, readonly=True)
    member_id = fields.Many2one('res.partner', string='Member', required=True)
    return_date = fields.Date(string='Return Date')

    def action_rent_book(self):
        # دابا كنسجلو التاريخ والحالة دقة وحدة
        self.book_id.write({
            'state': 'rented',
            'date_return': self.return_date
        })
        return {'type': 'ir.actions.act_window_close'}