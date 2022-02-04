# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime
from datetime import date
class titulo(models.Model):
    _name = 'saez.titulo'
    _description = 'saez.titulo'

    name = fields.Text(string="Titulo")

    alumnos_ids = fields.Many2many('saez.alumno',
                     'saez_titulo_alumno_rel',
                     'titulo_id',
                     'alumno_id',
                     string='Alumnos')

class alumno(models.Model):
    _name = 'saez.alumno'
    _description = 'saez.alumno'

    name = fields.Text(string="Nombre")
    apellido1 = fields.Text(string="Primer Apellido")
    apellido2 = fields.Text(string="Segundo Apellido")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')], string="Sexo")
    foto = fields.Image(string="Foto")

    pais_id = fields.Many2one('res.country', string='Pais')
    proyectos_ids = fields.One2many('saez.proyecto', 'alumno_id', string='Proyectos')

    titulos_ids = fields.Many2many('saez.titulo',
                                   'saez_titulo_alumno_rel',
                                   'alumno_id',
                                   'titulo_id',
                                   string='Titulos')



class proyecto(models.Model):
    _name = 'saez.proyecto'
    _description = 'saez.proyecto'

    name = fields.Text(string="Nombre Proyecto")
    descripcion = fields.Text(string="Descripcion")
    fecha_inicio = fields.Date(string="Fecha Inicio")
    fecha_entrega = fields.Date(string="Fecha Entrega")
    nota = fields.Integer(string="Nota")
    aprobado = fields.Boolean(string="Aprobado", compute="_comprobar_nota")
    proyecto_definitivo = fields.Boolean(string="Proyecto Definitivo", compute="_comprobar_proyecto_definivo")

    alumno_id = fields.Many2one('saez.alumno', string='Alumno')
    estado_id = fields.Many2one('saez.estado', string='Estado')
    asignatura_id = fields.Many2one('saez.asignatura', string='Asignatura', required=True)

    @api.constrains('nota')
    def _comprobar_formato_nota(self):
        print("\tFUNCTION _comprobar_formato_nota RUNNING (Proyecto)")
        #Implementar Codigo que valide que la nota no puede ser ni cero ni menos

    @api.onchange('nota')
    def _comprobar_nota(self):
        print("\tFUNCTION _comprobar_nota RUNNING (Proyecto)")
        if(self.nota):
            if(self.nota >= 5):
                self.aprobado = True
            else:
                self.aprobado = False
        else:
            self.aprobado = False

    def _comprobar_proyecto_definivo(self):
        print("\tFUNCTION _comprobar_proyecto_definivo RUNNING (Proyecto)")
        if (self.fecha_inicio):
            #Implementar Codigo
            fecha = self.fecha_inicio + datetime.timedelta(days=(10))
            fecha_hoy = date.today()
            print("\tfecha:" + str(fecha))
            print("\tfecha_hoy:" + str(fecha_hoy))
            if(fecha >= fecha_hoy):
                self.proyecto_definitivo = True
            else:
                self.proyecto_definitivo = False

        else:
            self.proyecto_definitivo = False


class estado(models.Model):
    _name = 'saez.estado'
    _description = 'saez.estado'

    name = fields.Text(string="Nombre")
    duracion = fields.Integer(string="Dias de Duracion")
    proyectos_ids = fields.One2many('saez.proyecto', 'estado_id', string='Proyectos')

class asignatura(models.Model):
    _name = 'saez.asignatura'
    _description = 'saez.asignatura'

    name = fields.Text(string="Nombre")
    proyectos_ids = fields.One2many('saez.proyecto', 'asignatura_id', string='Proyectos')

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Asignatura name already exists !')
    ]