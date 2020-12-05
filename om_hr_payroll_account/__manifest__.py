# -*- coding:utf-8 -*-

{
    'name': 'Odoo 14 HR Payroll Accounting',
    'category': 'Human Resources',
    'author': 'Odoo Mates, Odoo SA',
    'version': '14.0.2.0.0',
    'sequence': 1,
    'website': 'https://www.odoomates.tech',
    'summary': 'Generic Payroll system Integrated with Accounting',
    'description': """Generic Payroll system Integrated with Accounting.""",
    'depends': [
        'om_hr_payroll',
        'account'
    ],
    'data': [
        'views/hr_payroll_account_views.xml'
    ],
    'demo': [],
    'test': ['../account/test/account_minimal_test.xml'],
    'images': ['static/description/banner.png'],
    'application': True,
}
