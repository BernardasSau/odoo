{
    'name': 'Document Management',
    'version': '1.0',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/info_views.xml',
        'views/report_actions.xml',
        'views/report_templates.xml',
        'views/info_filter_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
}



