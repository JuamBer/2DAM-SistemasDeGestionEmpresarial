# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aab__autor(models.Model):
     _name = 'aab__autor.aab__autor'
     _description = 'aab__autor.aab__autor'

     nombre = fields.Char()
     edad = fields.Integer()
     foto = fields.Image()
     fecha_nacimiento = fields.Date()
     sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')])
     descripcion = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
