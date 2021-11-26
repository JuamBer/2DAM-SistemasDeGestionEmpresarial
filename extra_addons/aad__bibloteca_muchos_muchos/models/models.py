# -*- coding: utf-8 -*-
from odoo import models, fields, api

class libro(models.Model):
    _name = 'aad_bibloteca_muchos_muchos.libro'
    _description = 'aad_bibloteca_muchos_muchos.libro'

    name = fields.Char(string="Nombre", required=True)
    paginas = fields.Integer(string="Número de Páginas")


    editorial_id = fields.Many2one('aad_bibloteca_muchos_muchos.editorial', string='Editorial')
    autores_ids = fields.Many2many(
        'aad_bibloteca_muchos_muchos.autor',
        'aad_bibloteca_muchos_muchos_libro_autor_rel',
        'libro_id',
        'autor_id',
        string='Autores'
    )

class autor(models.Model):
    _name = 'aad_bibloteca_muchos_muchos.autor'
    _description = 'aad_bibloteca_muchos_muchos.autor'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    foto = fields.Image(string="Foto")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')], string="Sexo")
    descripcion = fields.Text(string="Descripción")

    libros_ids = fields.Many2many(
        'aad_bibloteca_muchos_muchos.libro',
        'aad_bibloteca_muchos_muchos_libro_autor_rel',
        'autor_id',
        'libro_id',
        string='Libros'
    )


class editorial(models.Model):
    _name = 'aad_bibloteca_muchos_muchos.editorial'
    _description = 'aad_bibloteca_muchos_muchos.editorial'

    name = fields.Char(string="Nombre", required=True)

    libros_ids = fields.One2many('aad_bibloteca_muchos_muchos.libro', 'editorial_id', string='Libros')