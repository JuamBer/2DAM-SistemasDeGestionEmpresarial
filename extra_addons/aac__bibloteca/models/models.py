# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Module Name: AAC_Bibloteca
# Classes:
#   libro (python) -> aac_bibloteca_libro (sql)
#   autor (python) -> aac_bibloteca_autor (sql)

class libro(models.Model):
     _name = 'aac_bibloteca.libro'
     _description = 'aac_bibloteca.libro'

     name = fields.Char()


class autor(models.Model):
    _name = 'aac_bibloteca.autor'
    _description = 'aac_bibloteca.autor'

    name = fields.Char()

