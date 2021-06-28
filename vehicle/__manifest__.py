# -*- coding: utf-8 -*-
#############################################################################
#
#   Tècniques d'Avantguarda
#
#############################################################################
{
    'name': "Vehicle manager",
    'version': '13.0.0.0.1',
    'summary': """Manage the vehicles from your contacts""",
    'description': """This Module Enables To manage the vehicles from your customers""",
    'author': "Tècniques d'Avantguarda",
    'company': "Tècniques d'Avantguarda",
    'website': "https://www.tda.ad",
    'category': 'other',
    'depends': ['base', 'account'],
    'data': [
        'views/menus.xml',
        'views/vehicle_view.xml'
        # 'views/invoice_stock_move_view.xml'
    ],
    # 'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
