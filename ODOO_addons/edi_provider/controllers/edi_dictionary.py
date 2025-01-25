from odoo import http
from odoo.http import request

class EdiDictionaryController(http.Controller):

    @http.route('/edi/dictionary', auth='public', website=True)
    def edi_dictionary(self, **kw):
        return request.render('edi_provider.edi_dictionary_template')
