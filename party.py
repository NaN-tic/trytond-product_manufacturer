#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta

class Party:
    """Party"""
    __name__ = 'party.party'

    manufacturer = fields.Boolean('Manufacturer',
        help="Check this box if the partner is a manufacturer.")
