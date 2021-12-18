# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, date

class inventario(models.Model):
    _name = 'aag__cesta_compra.inventario'
    _description = 'aag__cesta_compra.inventario'

    name = fields.Text(string="Nombre", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)
    tipo_producto = fields.Selection([('Abeto', 'Abeto'), ('Pino', 'Pino'), ('Roble', 'Roble')], string="Tipo De Producto", required=True)
    precio = fields.Float(string="Precio", required=True)

    ids_compras = fields.One2many('aag__cesta_compra.compra', 'id_inventario', string='Compras')

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Product name already exists !')
    ]
    _order = 'precio desc'

class comprador(models.Model):
    _name = 'aag__cesta_compra.comprador'
    _description = 'aag__cesta_compra.comprador'

    nif = fields.Text(string="NIF", required=True)
    nif_tutor = fields.Text(string="NIF Tutor")
    name = fields.Text(string="Nombre", required=True)
    apellido1 = fields.Text(string="Primer Apellido", required=True)
    apellido2 = fields.Text(string="Segundo Apellido", required=True)
    direccion = fields.Text(string="Dirección")
    fecha_nac = fields.Date(string="Fecha De Nacimiento")
    edad = fields.Integer(string="Edad", compute="_calcular_edad")
    dinero_gastado = fields.Float(string="Dinero Gastado", compute="_calcular_dinero_gastado")

    id_pais = fields.Many2one(comodel_name='res.country', string='Pais')
    ids_compras = fields.One2many('aag__cesta_compra.compra', 'id_comprador', string='Compras')

    _sql_constraints = [
        ('nif_uniq', 'UNIQUE(nif)', 'NIF already exists !')
    ]

    @api.depends('fecha_nac')
    def _calcular_edad(self):
        print("FUNCTION _calcular_edad RUNNING (Comprador)")
        today = date.today()
        birthdate = self.fecha_nac

        if birthdate:
            print("\tBirthdate:"+str(birthdate))
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            self.edad = age
            print("\tEdad: "+str(age))
        else:
            print("\tBirthdate: None")
            print("\tEdad: None")
            self.edad = None

    @api.depends('ids_compras')
    def _calcular_dinero_gastado(self):
        print("FUNCTION _calcular_dinero_gastado RUNNING (Comprador)")
        dinero_gastado = 0
        compras = self.ids_compras

        if compras:
            for compra in compras:
                nombre_producto = compra.id_inventario.name
                precio_producto = compra.id_inventario.precio
                cantidad_copmpra =  compra.cantidad
                coste_compra = precio_producto * cantidad_copmpra

                print("\tCompró " + str(cantidad_copmpra) + " unidades de " + str(nombre_producto) + " por " + str(precio_producto) + " cada unidad, un total de: " +str(coste_compra))
                dinero_gastado += coste_compra

            self.dinero_gastado = dinero_gastado
        else:
            print("\tNo hay compras")
            self.dinero_gastado = 0


class compra(models.Model):
    _name = 'aag__cesta_compra.compra'
    _description = 'aag__cesta_compra.compra'

    id_inventario = fields.Many2one(comodel_name='aag__cesta_compra.inventario', string='Inventario', required=True)
    id_comprador = fields.Many2one(comodel_name='aag__cesta_compra.comprador', string='Comprador', required=True)
    cantidad = fields.Integer(default=0, string="Cantidad", required=True)
    fecha = fields.Date(string="Date")

    @api.constrains('id_inventario')
    def _check_stock_exists(self):
        print("FUNCTION _check_stock_exists RUNNING (Compra)")
        if self.id_inventario.cantidad < 0:
            print("\tThere is not stock from " + str(self.id_inventario.name))
            raise ValidationError("There is not stock from "+str(self.id_inventario.name))
        else:
            print("\tStock of " + str(self.id_inventario.name) + " exists")

    @api.constrains('cantidad')
    def _check_stock_is_enough(self):
        print("FUNCTION _check_stock_is_enough RUNNING (Compra)")
        if self.id_inventario.cantidad < self.cantidad:
            print("\tNot enough stock: " + str(self.id_inventario.cantidad))
            raise ValidationError("Not enough stock: " + str(self.id_inventario.cantidad))
        else:
            print("\tEnough stock: " + str(self.id_inventario.cantidad))

    @api.onchange('cantidad')
    def _descontar_cantidad_inventario(self):
        print("FUNCTION _descontar_cantidad_inventario RUNNING (Compra)")

        cantidadInventarioSinDescontar = self.id_inventario.cantidad
        cantidadCompra = self.cantidad

        print("\tcantidadInventarioSinDescontar: " + str(cantidadInventarioSinDescontar))
        print("\tcantidadCompra: " + str(cantidadCompra))

        if cantidadInventarioSinDescontar >= cantidadCompra:
            self.id_inventario.cantidad = cantidadInventarioSinDescontar - cantidadCompra
            print("\tcantidadInventarioDescontado: " + str(cantidadInventarioSinDescontar - cantidadCompra))
        else:
            print("\tNada Descontado")

    def name_get(self):
        print("FUNCTION name_get RUNNING (Compra)")
        result = []
        for compra in self:
            name = compra.id_inventario.name + " " + compra.id_comprador.name
            print("\t" + name)
            result.append((compra.id, name))
        return result

