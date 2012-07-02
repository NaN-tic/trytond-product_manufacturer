#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class Party(ModelSQL, ModelView):
    """Party"""
    _name = 'party.party'
    _description = __doc__

    manufacturer = fields.Boolean('Manufacturer',
        help="Check this box if the partner is a manufacturer.")

Party()


