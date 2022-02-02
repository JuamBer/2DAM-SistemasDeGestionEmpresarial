#-*- coding: utf-8 -*-

from odoo import models, fields, api

class entity1(models.Model):
    _name = 'aak_examen.entity1'
    _description = 'aak_examen.entity1'

    name = fields.Char()
    value = fields.Integer()

class entity2(models.Model):
    _name = 'aak_examen.entity2'
    _description = 'aak_examen.entity2'

    name = fields.Char()
    value = fields.Integer()

class entity3(models.Model):
    _name = 'aak_examen.entity3'
    _description = 'aak_examen.entity3'

    name = fields.Char()
    value = fields.Integer()
