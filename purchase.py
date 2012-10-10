#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['PurchaseLine']
__metaclass__ = PoolMeta

class PurchaseLine:
    'Purchase Line'
    __name__ = 'purchase.line'

    manufacturer = fields.Function(
        fields.Many2One('party.party', 'Manufacturer',
            on_change=['product']),
        'get_manufacturer')

    @classmethod
    def get_manufacturer(cls, records, name):
        result = {}
        for line in records:
            result[line.id] = line.product.manufacturer.id
        return result

    def on_change_product(self):
        """When change product, get manufacturer value"""
        product_obj = Pool().get('product.product')
        res = super(PurchaseLine, self).on_change_product()
        product = self.product or  False
        res['manufacturer'] = None
        if self.product:
            product = self.product
            res['manufacturer'] = product.manufacturer and \
                    product.manufacturer.id or None
        return res

