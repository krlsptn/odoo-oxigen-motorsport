# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VehicleOwnerRegister(models.Model):
    _name = 'vehicle.owner.register'

    date_of_transaction = fields.Date()
    res_partner_id = fields.Many2one('res.partner')
    vehicle_id = fields.Many2one('vehicle')
    note = fields.Text()


class VehicleNote(models.Model):
    _name = 'vehicle.note'

    date_note = fields.Date(required=True)
    title = fields.Char(required=True)
    description = fields.Text()
    vehicle_id = fields.Many2one('vehicle', required=True)


class VehicleBrand(models.Model):
    _name = 'vehicle.brand'
    _rec_name = 'brand'

    brand = fields.Char(required=True)


class VehicleBrandModel(models.Model):
    _name = 'vehicle.brand.model'

    brand_model = fields.Char(required=True)
    vehicle_brand_id = fields.Many2one('vehicle.brand', required=True)


class Vehicle(models.Model):
    _name = 'vehicle'
    _description = 'Vehicle'
    _order = 'vehicle_registration'
    _rec_name = 'vehicle_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    vehicle_name = fields.Char(compute='_compute_vehicle_name', store=True)
    owner_res_partner_id = fields.Many2one('res.partner')
    owner_name = fields.Char(related='owner_res_partner_id.name')

    vehicle_brand_id = fields.Many2one('vehicle.brand')
    vehicle_brand_model_id = fields.Many2one('vehicle.brand.model')  # faltara el domain

    vehicle_registration = fields.Char()
    vehicle_manufacturing_year = fields.Integer()
    vehicle_cubic_centimetres_size = fields.Integer()
    vehicle_horsepower = fields.Integer()
    vehicle_first_registration_date = fields.Date()
    vehicle_general_note = fields.Text()
    vehicle_kilometers = fields.Integer()

    vehicle_note_ids = fields.One2many('vehicle.note', 'vehicle_id')
    invoice_move_ids = fields.One2many('account.move', 'vehicle_id')
    last_invoice_move_id = fields.Many2one('account.move', compute='_compute_last_invoice_move_id', store=True)
    vehicle_owner_registration_ids = fields.One2many('vehicle.owner.register', 'vehicle_id')

    @api.depends('invoice_move_ids')
    def _compute_last_invoice_move_id(self):
        for this in self:
            if this.invoice_move_ids:
                last_invoice = False
                for invoice in this.invoice_move_ids:
                    if invoice.state == 'posted':
                        if not last_invoice:
                            last_invoice = invoice
                        else:
                            if this.last_invoice_move_id.invoice_date > last_invoice.invoice_date:
                                last_invoice = invoice
                this.last_invoice_move_id = last_invoice

    @api.depends('vehicle_registration', 'owner_name')
    def _compute_vehicle_name(self):
        for this in self:
            if this.owner_name:
                this.vehicle_name = '%s - %s' % (this.vehicle_registration, this.owner_name)
