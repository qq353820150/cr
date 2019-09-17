# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '企业文化',
    'version': '1.0',
    'category': 'Cust',
    'summary': '企业文化',
    'author': 'lqy',
    #'website': 'https://www.odoowww.com',
    'description': """
Beijing Railway Customer 
===========================================================================
京铁商服-企业文化


    """,
    'depends': ['base' ],
    'data': [
        'security/ir.model.access.csv',
        # 'data/cr_base.xml',
        'views/cr_ldjh.xml',
        'views/cr_qyxc.xml',
        #'wizard/hr_expense_check.xml',
    ],
    'demo': [
        #
        #
    ],
    'installable': True,
    'auto_install': False,
}
