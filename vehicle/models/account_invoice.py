# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move']

    vehicle_id = fields.Many2one('vehicle')
