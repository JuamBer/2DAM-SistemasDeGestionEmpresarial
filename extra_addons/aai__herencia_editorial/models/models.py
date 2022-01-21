# -*- coding: utf-8 -*-

from odoo import models, fields, api


# Module Name: AAI_HerenciaEditorial
# Classes:
#   libro (python) -> aah__herencia_libro_autor_libro (sql)
#   autor (python) -> aah__herencia_libro_autor_autor (sql)

class editorial(models.Model):
    _name = 'aai_herencia_editorial.editorial'
    _description = 'aai_herencia_editorial.editorial'

    name = fields.Char(string="Nombre", required=True)

    libros_ids = fields.One2many('aah_herencia_libro_autor.libro','editorial_id', string='Libros')