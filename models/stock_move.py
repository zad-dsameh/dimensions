# -*- coding: utf-8 -*-

from odoo import api, models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_dimension = fields.Char(string='Dimension:')


