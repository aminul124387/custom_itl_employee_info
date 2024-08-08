# -*- coding: utf-8 -*-

{
    'name': 'Employees Custom Info',
    'author': 'Md. Aminul Islam',
    'version': '16.0',
    'category': 'Human Resources Management',
    'sequence': 85,
    'summary': """Employee education
                  Experience, Skills Auto Employee creation When user create""",
    'maintainer': 'Md. Aminul Islam',
    'website': 'https://www.odoo.com',
    'description': """
        This module adds a valuable addition to the existing functionality of the Odoo HR module.
        By displaying the employee's education and experience in separate tree views, a more comprehensive views of an employee's qualifications, skills and work history will be provided.Auto Create Employee when create users""",
    'license': 'OPL-1',
    'support': 'aminul124387@gmail.com',
    'depends': ['base', 'hr', 'mail', 'hr_gamification', 'hr_contract', 'hr_skills'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/employee_creation_from_user_view.xml',
        'views/contract_days_view.xml',
        'views/hr_employee_member_view.xml',
        'views/updation_config.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
