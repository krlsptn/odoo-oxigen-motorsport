# -*- coding: utf-8 -*-

from odoo.exceptions import UserError
from odoo import models, fields, api, _


class VehicleNote(models.Model):
    _name = 'vehicle.note'

    date_note = fields.Date()
    title = fields.Char()
    description = fields.Text()
    vehicle_id = fields.Many2one('vehicle')


class VehicleBrand(models.Model):
    _name = 'vehicle.brand'

    brand = fields.Char(required=True)


class VehicleBrandModel(models.Model):
    _name = 'vehicle.brand.model'

    brand_model = fields.Char()
    vehicle_brand_id = fields.Many2one('vehicle.brand', required=True)


class Vehicle(models.Model):
    _name = 'vehicle'
    _description = 'Vehicle'
    _order = 'vehicle_registration'
    _rec_name = 'vehicle_name'

    vehicle_name = fields.Char(compute='_compute_vehicle_name', store=True)
    owner_res_partner_id = fields.Many2one('res.contact')
    owner_name = fields.Char(compute='_compute_owner_name', store=True)

    vehicle_registration = fields.Char()
    vehicle_manufacturing_year = fields.Integer()
    vehicle_cubic_centimetres_size = fields.Integer()
    vehicle_horsepower = fields.Integer()
    vehicle_first_registration_date = fields.Date()
    vehicle_general_note = fields.Text()
    vehicle_note_ids = fields.One2many('vehicle.note', 'vehicle_id')
    vehicle_brand_id = fields.Many2one('vehicle.brand')
    vehicle_brand_model_id = fields.Many2one('vehicle.brand.model')  # faltara el domain

    @api.depends('owner_res_partner_id')
    def _compute_owner_name(self):
        for this in self:
            pass

    @api.depends('vehicle_registration', 'owner_name')
    def _compute_vehicle_name(self):
        for this in self:
            pass













