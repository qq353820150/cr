# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '现场检查',
    'version': '1.0',
    'category': 'Cust',
    'summary': '现场检查',
    'author': 'lqy',
    #'website': 'https://www.odoowww.com',
    'description': """
Beijing Railway Customer 
===========================================================================
京铁商服-现场检查


    """,
    'depends': ['base','cr_base' ],
    'data': [
        'security/ir.model.access.csv',
        'views/cr_check_record.xml',
    ],
    'demo': [
        #
        #
    ],
    'installable': True,
    'auto_install': False,
}
