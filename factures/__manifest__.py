# -*- coding: utf-8 -*-
{
    'name': "factures",

    # any module necessary for this one to work correctly
    'depends': ['base', 'gestio_clients', 'articles', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'reports/report_factura.xml',
        'views/factura_report.xml',
        'data/ir_sequence.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}

