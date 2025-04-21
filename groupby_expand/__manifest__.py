{
    'name': 'GroupBy Expand Button',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Adds an Expand All Groups button in list view toolbar',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'groupby_expand/static/src/js/groupby_expand.js',
            'groupby_expand/static/src/xml/groupby_expand.xml',
        ],
    },
    'installable': True,
    'application': False,
}
