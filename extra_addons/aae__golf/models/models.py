# -*- coding: utf-8 -*-
from odoo import models, fields, api

class patrocinador(models.Model):
    _name = 'aae_golf.patrocinador'
    _description = 'aae_golf.patrocinador'

    name = fields.Char(string="Nombre", required=True)
    ids_torneos = fields.Many2many(
        'aae_golf.torneo',
        'aae_golf_torneo_patrocinador_rel',
        'patrocinador_id',
        'torneo_id',
        string='Torneos'
    )

class campo(models.Model):
    _name = 'aae_golf.campo'
    _description = 'aae_golf.campo'

    name = fields.Char(string="Nombre", required=True)
    direccion = fields.Text(string="Dirección")


class hoyo(models.Model):
    _name = 'aae_golf.hoyo'
    _description = 'aae_golf.hoyo'

    name = fields.Char(string="Nombre", required=True)
    par = fields.Integer(string="Par")
    dificultad = fields.Selection([('Baja','Baja'), ('Media','Media'), ('Alta','Alta')])
    id_campo = fields.Many2one('aae_golf.campo', string='Campo')

class participante(models.Model):
    _name = 'aae_golf.participante'
    _description = 'aae_golf.participante'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    pais = fields.Many2one('res.country', string='Pais')


class torneo(models.Model):
    _name = 'aae_golf.torneo'
    _description = 'aae_golf.torneo'

    name = fields.Char(string="Nombre", required=True)
    year = fields.Integer(string="Año")
    id_campo = fields.Many2one('aae_golf.campo', string='Campo', required=True)
    ids_patrocinadores = fields.Many2many(
        'aae_golf.patrocinador',
        'aae_golf_torneo_patrocinador_rel',
        'torneo_id',
        'patrocinador_id',
        string='Patrocinadores'
    )

class puntos(models.Model):
    _name = 'aae_golf.puntos'
    _description = 'aae_golf.puntos'

    id_torneo = fields.Many2one('aae_golf.torneo', string='Torneo', required=True)
    id_participante = fields.Many2one('aae_golf.participante', string='Participante', required=True)
    id_hoyo = fields.Many2one('aae_golf.hoyo', string='Hoyo', required=True)
    dia = fields.Integer(string="Dia", required=True)
    golpes = fields.Integer(string="Golpes", required=True)