# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class patrocinador(models.Model):
    _name = 'aaf_golf_view.patrocinador'
    _description = 'aaf_golf_view.patrocinador'

    name = fields.Char(string="Nombre", required=True)
    ids_torneos = fields.Many2many(
        'aaf_golf_view.torneo',
        'aaf_golf_torneo_patrocinador_rel',
        'patrocinador_id',
        'torneo_id',
        string='Torneos'
    )


class campo(models.Model):
    _name = 'aaf_golf_view.campo'
    _description = 'aaf_golf_view.campo'

    name = fields.Char(string="Nombre", required=True)
    direccion = fields.Text(string="Dirección")


class hoyo(models.Model):
    _name = 'aaf_golf_view.hoyo'
    _description = 'aaf_golf_view.hoyo'

    name = fields.Char(string="Nombre", required=True)
    par = fields.Integer(string="Par")
    dificultad = fields.Selection([('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')])
    id_campo = fields.Many2one('aaf_golf_view.campo', string='Campo')


class participante(models.Model):
    _name = 'aaf_golf_view.participante'
    _description = 'aaf_golf_view.participante'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    pais = fields.Many2one('res.country', string='Pais')


class torneo(models.Model):
    _name = 'aaf_golf_view.torneo'
    _description = 'aaf_golf_view.torneo'

    name = fields.Char(string="Nombre", required=True)
    start_date = fields.Date(string="Fecha de Inicio")
    end_date = fields.Date(string="Fecha de Fin")
    id_campo = fields.Many2one('aaf_golf_view.campo', string='Campo', required=True)
    ids_patrocinadores = fields.Many2many(
        'aaf_golf_view.patrocinador',
        'aaf_golf_torneo_patrocinador_rel',
        'torneo_id',
        'patrocinador_id',
        string='Patrocinadores'
    )



class puntos(models.Model):
    _name = 'aaf_golf_view.puntos'
    _description = 'aaf_golf_view.puntos'

    id_torneo = fields.Many2one('aaf_golf_view.torneo', string='Torneo', required=True)
    id_participante = fields.Many2one('aaf_golf_view.participante', string='Participante', required=True)
    id_hoyo = fields.Many2one('aaf_golf_view.hoyo', string='Hoyo', required=True)
    dia = fields.Integer(string='Dia', default='1', required=True)
    golpes = fields.Integer(string='Golpes', required=True)
    date = fields.Date(string='Fecha', compute='_calcular_fecha')

    @api.depends('dia','id_torneo.start_date')
    def _calcular_fecha(self):
        print("FUNCTION _calcular_fecha RUNNING")
        if self.id_torneo:
            print("\tExiste Torneo")
            if self.id_torneo.start_date:
                self.date = self.id_torneo.start_date + datetime.timedelta(days=(self.dia - 1))
                print("\t" + str(self.date))
            else:
                print("\tNo Existe start_date")
        else:
            self.date = datetime.date.today()
            print("\tNo Existe Torneo")

    def name_get(self):
        print("FUNCTION name_get RUNNING")
        result = []
        for punto in self:
            name = punto.id_torneo.name + " " + punto.id_participante.name + " " + punto.id_hoyo.name
            print("\t" + name)
            result.append((punto.id,name))
        return result