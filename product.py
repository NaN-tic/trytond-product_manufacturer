#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['ProductTemplate', 'ProductProduct']
__metaclass__ = PoolMeta

class ProductTemplate:
    'Product Template'
    __name__ = 'product.template'

    manufacturer = fields.Many2One('party.party', 'Manufacturer',
        domain=[('manufacturer', '=', True)])

class ProductProduct:
    'Product Product'
    __name__ = 'product.product'

    manufacturer_name =  fields.Char('Manufacturer Name')
    manufacturer_code =  fields.Char('Manufacturer Code')
