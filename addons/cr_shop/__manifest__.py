# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '商业点位',
    'version': '1.0',
    'category': 'Cust',
    'summary': '商业点位',
    'author': 'yuejian',
    #'website': 'https://www.odoowww.com',
    'description': """
Beijing Railway Customer 
===========================================================================
京铁商服-商业点位


    """,
    'depends': ['base','cr_base'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/cr_base.xml',
        'views/cr_sydw.xml',
        'views/cr_cyry.xml',
        'views/cr_ydss.xml',
        'views/cr_xfss.xml',
        #'wizard/hr_expense_check.xml',
    ],
    'demo': [
        #
        #
    ],
    'installable': True,
    'auto_install': False,
}
