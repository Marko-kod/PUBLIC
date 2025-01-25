{
    'name': 'EDI Provider Management',
    'version': '1.0',
    'summary': 'Module for managing EDI providers and their communication settings.',
    'author': 'Marko Korenić',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'depends': ['base', 'website'],  # Ensure 'website' is included if you're using website features
    'data': [
        'security/ir.model.access.csv',
        'views/edi_provider_views.xml',
        'views/edi_format_views.xml',        
        'views/edi_dictionary_menu.xml',
        'views/edi_dictionary_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # Typically, backend assets like JS or CSS are included here
            # If you have such assets, list them; otherwise, this can be omitted
        ],
        'web.assets_frontend': [
            # If you have frontend assets, list them here
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],  # Ensure this image exists at the specified path
}
