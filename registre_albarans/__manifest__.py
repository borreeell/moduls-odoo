# -*- coding: utf-8 -*-
{
    'name': "registre_albarans",

    # Moduls del que depen aquest modul
    'depends': ['base', 'gestio_clients', 'articles'],

    # Arxius que es carreguen
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/ir_sequence.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}

