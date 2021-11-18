# -*- coding: utf-8 -*-
from odoo import models, fields, api

class aab__autor(models.Model):
     _name = 'aab__autor.aab__autor'
     _description = 'aab__autor.aab__autor'

     nombre = fields.Char(string="Nombre", required=True)
     edad = fields.Integer(string="Edad")
     foto = fields.Image(string="Foto")
     fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
     sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')],string="Sexo")
     descripcion = fields.Text(string="Descripción")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


#from odoo import models, fields, api

#class aab__libro(models.Model):
#     _name = 'aab__libro.aab__libro'
#     _description = 'aab__libro.aab__libro'
#
#     nombre = fields.Char(string="Nombre", required=True)
#     edad = fields.Integer(string="Edad")
#     foto = fields.Image(string="Foto")
#     fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
#     sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')],string="Sexo")
#     descripcion = fields.Text(string="Descripción")