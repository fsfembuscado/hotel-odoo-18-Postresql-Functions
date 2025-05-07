# -*- coding: utf-8 -*-
# roomtypes.py

from odoo import models, fields, api

class RoomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types Master List'

    # Room type name
    name = fields.Char("Room Type", required=True)
    
    # Description of the room type
    description = fields.Text("Room Type Description")
    
    # Images for the room and bathroom
    room_image = fields.Image("Room Image")
    bathroom_image = fields.Image("Bathroom Image")
    
    # Daily charges for the room type
    daily_charges = fields.Float("Daily Charges")
    
    # One2many relationship with hotel rooms
    room_ids = fields.One2many('hotel.rooms', 'roomtype_id', string="Rooms")


# # -*- coding: utf-8 -*-
# # roomtypes.py

# from odoo import models, fields, api

# class roomTypes(models.Model):
#     _name = 'hotel.roomtypes'
#     _description = 'Hotel Room Types Master List'

#     name = fields.Char("Room Type", required=True)
#     description = fields.Char("Room Type Description")
    
#     room_image = fields.Image("Room Image")
#     bathroom_image = fields.Image("Bathroom Image")
    
#     daily_charges = fields.Float("Daily Charges")
    
#     room_ids = fields.One2many('hotel.rooms', 'roomtype_id', string="Rooms")