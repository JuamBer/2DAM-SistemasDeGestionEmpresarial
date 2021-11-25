# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Module Name: AAC_Bibloteca
# Classes:
#   libro (python) -> aac_bibloteca_libro (sql)
#   autor (python) -> aac_bibloteca_autor (sql)
#   editorial (python) -> aac_bibloteca_editorial (sql)

class libro(models.Model):
     _name = 'aac_bibloteca.libro'
     _description = 'aac_bibloteca.libro'

     name = fields.Char(string="Nombre", required=True)
     paginas = fields.Integer(string="Número de Páginas")

     autor_id = fields.Many2one('aac_bibloteca.autor', string='Autor')
     editorial_id = fields.Many2one('aac_bibloteca.editorial', string='Editorial')

class autor(models.Model):
    _name = 'aac_bibloteca.autor'
    _description = 'aac_bibloteca.autor'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    foto = fields.Image(string="Foto")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')], string="Sexo")
    descripcion = fields.Text(string="Descripción")

    libros_ids = fields.One2many('aac_bibloteca.libro','autor_id', string='Libros')

class editorial(models.Model):
    _name = 'aac_bibloteca.editorial'
    _description = 'aac_bibloteca.editorial'

    name = fields.Char(string="Nombre", required=True)

    libros_ids = fields.One2many('aac_bibloteca.libro','editorial_id', string='Libros')

