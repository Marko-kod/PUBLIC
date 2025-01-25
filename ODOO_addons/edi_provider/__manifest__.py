{
    'name': 'EDI Provider Management',
    'version': '1.0',
    'summary': 'Module for managing EDI providers and their communication settings.',
    'author': 'Marko Korenić',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/edi_provider_views.xml',
        'views/edi_format_views.xml',
        'views/edi_dictionary_views.xml',   # ✅ Include the new menu file
        'views/edi_dictionary_template.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'edi_provider/static/html/edi_dictionary.html',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],  # Dodaj ovu liniju!
}
