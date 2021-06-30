# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move']

    vehicle_id = fields.Many2one('vehicle', domain="[('owner_res_partner_id', '=', partner_id)]")
    vehicle_invoice_date = fields.Date(compute='_compute_vehicle_invoice_date')

    def _compute_vehicle_invoice_date(self):
        for this in self:
            if this.invoice_date:
                this.vehicle_invoice_date = this.invoice_date
            else:
                this.vehicle_invoice_date = None
