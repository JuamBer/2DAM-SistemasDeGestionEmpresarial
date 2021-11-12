# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aaa__hola_mundo(models.Model):
    _name = 'aaa__hola_mundo.aaa__hola_mundo'
    _description = 'aaa__hola_mundo.aaa__hola_mundo'

    nombre = fields.Char()
    edad = fields.Integer()
    foto = fields.Image()
    fecha_nacimiento = fields.Date()
    sexo = fields.Selection([('Hombre','Hombre'),('Mujer','Mujer')])
    descripcion = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
