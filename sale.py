#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class SaleLine(ModelSQL, ModelView):
    'Sale Line'
    _name = 'sale.line'
    _description = __doc__

    manufacturer = fields.Function(
        fields.Many2One('party.party', 'Manufacturer',
            on_change=['product']),
        'get_manufacturer')

    def get_manufacturer(self, ids, name):
        result = {}
        for line in self.browse(ids):
            result[line.id] = line.product.manufacturer.id
        return result

    def on_change_product(self, values):
        """When change product, get manufacturer value"""
        product_obj = Pool().get('product.product')
        res = super(SaleLine, self).on_change_product(values)
        product = values.get('product', False)
        res['manufacturer'] = None
        if values.get('product'):
            product = product_obj.browse(values['product'])
            res['manufacturer'] = product.manufacturer and \
                    product.manufacturer.id or None
        return res

SaleLine()
