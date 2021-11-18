# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Module Name: AAA_HolaMundo
# Classes:
#   aaa__hola_mundo (python) -> aaa__hola_mundo.aaa__hola_mundo (sql)

class aaa__hola_mundo(models.Model):
    _name = 'aaa__hola_mundo.aaa__hola_mundo'
    _description = 'aaa__hola_mundo.aaa__hola_mundo'

    nombre = fields.Char()
    edad = fields.Integer()
    foto = fields.Image()
    fecha_nacimiento = fields.Date()
    sexo = fields.Selection([('Hombre','Hombre'),('Mujer','Mujer')])
    descripcion = fields.Text()
