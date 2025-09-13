# copyright 2025 Loïc TEKEU (Alt Plus)
# License OPL-1 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'POS Order Limit',
    'version': '16.0.1.0.0',
    'summary': 'Limit the number of pending orders in the Point of Sale',
    'description': """
This module prevents the creation of new POS orders when the number of pending orders reaches a configured limit.
It helps avoid overload and ensures better cashier workflow management.
""",
    'category': 'Point of Sale',
    'author': 'Loïc TEKEU (Alt Plus)',
    'website': 'https://github.com/tekeu10',
    'support': 'https://www.linkedin.com/in/lo%C3%AFc-cabrel-tekeu-1b7b9125b',
    'license': 'OPL-1',
    'price': 34.99,
    'currency': 'EUR',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_order_limit/static/src/js/pos_order_limit.js',
        ],
    },
    'installable': True,
    'application': False,
}