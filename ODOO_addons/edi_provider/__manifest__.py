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

    ],

 
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],  # Ensure this image exists at the specified path
}
