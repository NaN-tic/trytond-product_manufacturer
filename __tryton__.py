#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Product Manufactuer',
    'name_ca_ES': 'Fabricant del producte',
    'name_es_ES': 'Fabricante del producto',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Add manufactruer information: manufacturer, name and code
''',
    'description_ca_ES': '''Afegeix informació del fabricant al producte: fabricant, nom i codi
''',
    'description_es_ES': '''Añade información del fabricante al producto: fabricante, nombre y código
''',
    'depends': [
        'ir',
        'res',
        'product',
        'purchase',
        'sale',
        'stock',
    ],
    'xml': [
        'move.xml',
        'party.xml',
        'product.xml',
        'purchase.xml',
        'sale.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
