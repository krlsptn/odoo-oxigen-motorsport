# -*- coding: utf-8 -*-
#############################################################################
#
#   Tècniques d'Avantguarda
#
#############################################################################
{
    'name': "Vehicle manager",
    'version': '13.0.0.0.3',
    'summary': """Manage the vehicles from your contacts""",
    'author': "Tècniques d'Avantguarda",
    'company': "Tècniques d'Avantguarda",
    'website': "https://www.tda.ad",
    'category': 'Specific Industry Applications',
    'depends': ['account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/vehicle_brand_data.xml',
        'views/vehicle_views.xml',
        'views/account_invoice_views.xml',
        'views/menus.xml',
    ],
    # 'license': 'AGPL-3',
    'installable': True,
    # 'auto_install': False,
    'application': True,
}
