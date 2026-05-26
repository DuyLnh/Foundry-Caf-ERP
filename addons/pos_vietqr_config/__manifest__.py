{
    'name': 'POS VietQR Config',
    'version': '1.2',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': ['views/pos_config_views.xml'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_vietqr_config/static/src/xml/order_receipt.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}