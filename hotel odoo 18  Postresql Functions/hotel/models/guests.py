# -*- coding: utf-8 -*-
# guests.py

from odoo import models, fields, api
from datetime import date

class Guests(models.Model):
    _name = 'hotel.guests'
    _description = 'Hotel Guests'

    lastname = fields.Char("Lastname")
    firstname = fields.Char("Firstname")
    middlename = fields.Char("Middlename")
    address_streetno = fields.Char("Address/ Street & No.")
    address_area = fields.Char("Address / Area, Unit & Bldg, Brgy")
    address_city = fields.Char("Address / City/Town")
    address_province = fields.Char("Address / Province/State")
    zipcode = fields.Char("ZIP Code")
    contactno = fields.Char("Contact No.")
    email = fields.Char("Email")
    gender = fields.Selection([('FEMALE', 'Female'), ('MALE', 'Male')], string="Gender")
    birthdate = fields.Date("BirthDate")
    photo = fields.Image("Guest Photo")

    name = fields.Char(string='Guest Name', compute='_compute_name', store=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('firstname', 'lastname', 'middlename')
    def _compute_name(self):
        for rec in self:
            parts = [rec.lastname or '', rec.firstname or '', rec.middlename or '']
            rec.name = ', '.join(filter(None, [parts[0], parts[1]])) + (f' {parts[2]}' if parts[2] else '')

    @api.depends('birthdate')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.birthdate:
                rec.age = today.year - rec.birthdate.year - ((today.month, today.day) < (rec.birthdate.month, rec.birthdate.day))
            else:
                rec.age = 0
