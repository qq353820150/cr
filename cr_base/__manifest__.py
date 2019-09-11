# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '系统信息',
    'version': '1.0',
    'category': 'Cust',
    'summary': '系统信息',
    'author': 'lqy',
    #'website': 'https://www.odoowww.com',
    'description': """
Beijing Railway Customer 
===========================================================================
京铁商服-系统信息


    """,
    'depends': ['base' ],
    'data': [
        'security/ir.model.access.csv',
        # 'data/cr_base.xml',
        'views/cr_base_fault.xml',
        'views/cr_base_project.xml',
        'views/cr_base_location.xml',
        #'wizard/hr_expense_check.xml',
    ],
    'demo': [
        #
        #
    ],
    'installable': True,
    'auto_install': False,
}
