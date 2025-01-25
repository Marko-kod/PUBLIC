from odoo import models, fields

class EDIFormat(models.Model):
    _name = 'edi.format'
    _description = 'EDI Format'

    name = fields.Char(string="Format Name", required=True)
    format_type = fields.Selection([
        ('xml', 'XML'),
        ('json', 'JSON'),
        ('csv', 'CSV')
    ], string="Format Type", required=True)
    description = fields.Text(string="Description")
