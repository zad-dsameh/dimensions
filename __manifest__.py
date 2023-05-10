# -*- coding: utf-8 -*-
{
    'name': "Dimensions",
    'summary': "Dimensions task",
    'description': """
    Dimensions task in three modules: Sale, Inventory, and Invoicing Module
     """,
    'author': "Dina Sameh",
    'website': "http://www.zadsolutions.com",
    'category': 'Dimensions',
    'version': '15.0.0.0.1',
    'depends': [
        'sale', 'stock', 'account',
    ],
    'data': [
        'views/sale_order_line_view.xml',
        'views/stock_move_view.xml',
        'views/account_invoice_line_view.xml',

    ],
    # our module is a submodule from purchases, so it is not a stand-alone application for this reason
    # we will set False as a value for application and if we made it false sequence wouldn't effect on our module
    'application': False,
    'license': 'LGPL-3',
}
