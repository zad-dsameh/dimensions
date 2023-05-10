# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_dimension = fields.Char(string='Dimension:', readonly=True)

