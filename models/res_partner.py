from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    member_type = fields.Selection([
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ], string='Member Type')
    
    cin_number = fields.Char(string='CIN Number')