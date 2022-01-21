# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Module Name: AAH_HerenciaLibroAutor
# Classes:
#   libro (python) -> aah__herencia_libro_autor_libro (sql)
#   autor (python) -> aah__herencia_libro_autor_autor (sql)

class libro(models.Model):
     _name = 'aah_herencia_libro_autor.libro'
     _description = 'aah_herencia_libro_autor.libro'

     name = fields.Char(string="Nombre", required=True)
     paginas = fields.Integer(string="Número de Páginas")

     autor_id = fields.Many2one('aah_herencia_libro_autor.autor', string='Autor')

class autor(models.Model):
    _name = 'aah_herencia_libro_autor.autor'
    _description = 'aah_herencia_libro_autor.autor'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    foto = fields.Image(string="Foto")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')], string="Sexo")
    descripcion = fields.Text(string="Descripción")

    libros_ids = fields.One2many('aah_herencia_libro_autor.libro','autor_id', string='Libros')
