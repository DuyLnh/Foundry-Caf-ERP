{
    'name': 'POS Kitchen Order Ticket',
    'version': '1.1',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'pos_kot/static/src/xml/kot_receipt.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}