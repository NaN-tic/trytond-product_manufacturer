#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Move']
__metaclass__ = PoolMeta


class Move:
    __name__ = 'stock.move'
    manufacturer = fields.Function(
        fields.Many2One('party.party', 'Manufacturer'), 'get_manufacturer')

    @classmethod
    def get_manufacturer(cls, records, name):
        result = {}
        for line in records:
            result[line.id] = line.product.manufacturer and \
                line.product.manufacturer.id or None
        return result

    def on_change_product(self):
        """When change product, get manufacturer value"""
        res = super(Move, self).on_change_product()
        product = self.product or  False
        res['manufacturer'] = None
        if self.product:
            product = self.product
            res['manufacturer'] = product.manufacturer and \
                    product.manufacturer.id or None
        return res
