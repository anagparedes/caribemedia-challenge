{
    'name': 'caribemedia_contacts',
    'version': '15.0.1.0.0',
    'author': 'Caribe Media',
    'category': 'CRM',
    'depends': ['base', 'contacts'],
    'summary': 'Adds functionality to manage multiple phone numbers for clients.',
     'data': [
        'security/caribemedia_security.xml',
        'security/ir.model.access.csv',
        'views/contact_views.xml',
    ],
}
