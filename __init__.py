#This file is part product_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .move import *
from .party import *
from .product import *
from .purchase import *
from .sale import *


def register():
    Pool.register(
        Move,
        Party,
        ProductTemplate,
        ProductProduct,
        PurchaseLine,
        SaleLine,
        module='product_manufacturer', type_='model')
