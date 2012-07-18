#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Eval

class ProductTemplate(ModelSQL, ModelView):
    'Product Template'
    _name = 'product.template'
    _description = __doc__

    manufacturer = fields.Many2One('party.party', 'Manufacturer',
        domain=[('manufacturer', '=', True)])

ProductTemplate()

class ProductProduct(ModelSQL, ModelView):
    'Product Product'
    _name = 'product.product'
    _description = __doc__

    manufacturer_name =  fields.Char('Manufacturer Name')
    manufacturer_code =  fields.Char('Manufacturer Code')

ProductProduct()
