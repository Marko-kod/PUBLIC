from odoo import models, fields

class EDIQA(models.Model):
    _name = 'edi.qa'
    _description = 'EDI Questions and Answers'

    question = fields.Char(string="Question", required=True)
    answer = fields.Text(string="Answer", required=True)
    category = fields.Selection([
        ('technical', 'Technical'),
        ('business', 'Business'),
        ('integration', 'Integration'),
    ], string="Category", required=True)
