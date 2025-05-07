# -*- coding: utf-8 -*-
# rooms.py

from odoo import models, fields, api

class Rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Hotel Rooms'

    # Room number or name
    name = fields.Char("Room No.", required=True)
    
    # Description for the room
    description = fields.Text("Room Description")

    # Many2one relationship with room types (hotel.roomtypes)
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type", required=True)
    
    # Default order for sorting rooms by room number
    _order = 'name'

    # Related field for the room type name (for easier display or filtering)
    roomtype_name = fields.Char(related='roomtype_id.name', string="Room Type Name", store=True)


# # -*- coding: utf-8 -*-
# # rooms.py

# from odoo import models, fields, api

# class rooms(models.Model):
#     _name = 'hotel.rooms'
#     _description = 'Hotel Rooms'

#     name = fields.Char("Room No.")
#     description = fields.Char("Room Description")

#     roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type", required=True)
    
#     _order = 'name'
    
#     roomtype_name = fields.Char(related='roomtype_id.name', string ="Room Type Name", store=True)