# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Module Name: AAB_Autor
# Classes:
#   aab__autor (python) -> aab__autor.aab__autor (sql)

class aab__autor(models.Model):
     _name = 'aab__autor.aab__autor'
     _description = 'aab__autor.aab__autor'

     nombre = fields.Char(string="Nombre", required=True)
     edad = fields.Integer(string="Edad")
     foto = fields.Image(string="Foto")
     fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
     sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')],string="Sexo")
     descripcion = fields.Text(string="Descripción")



