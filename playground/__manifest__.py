# module_playground/__manifest__.py

{
    'name': 'Playground Rates',
    'version': '1.0',
    'summary': 'Manage Playground Rates from API',
    'description': 'Users can view and manage playground rates. Includes list, form, search, and kanban views with chatter.',
    'category': 'Custom',
    'depends': ['base', 'mail'],
    'data': [
        'report/report_playground.xml',
        'views/playground_rate_views.xml',
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
