from odoo import http
from odoo.http import request

class EDIDictionaryController(http.Controller):
    
    @http.route('/edi_provider/edi_dictionary', type='http', auth='public', website=True)
    def edi_dictionary_page(self, **kwargs):
        return request.render('edi_provider.edi_dictionary_template', {})
