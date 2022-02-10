# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, date

class inventario(models.Model):
    _name = 'aak_seguridad.inventario'
    _description = 'aak_seguridad.inventario'

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
    _name = 'aak_seguridad.comprador'
    _description = 'aak_seguridad.comprador'

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
    ids_compras = fields.One2many('aak_seguridad.compra', 'id_comprador', string='Compras')

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
    _name = 'aak_seguridad.compra'
    _description = 'aak_seguridad.compra'


    id_inventario = fields.Many2one(comodel_name='aak_seguridad.inventario', string='Inventario', required=True)
    id_comprador = fields.Many2one(comodel_name='aak_seguridad.comprador', string='Comprador', required=True)
    cantidad = fields.Integer(default=0, string="Cantidad", required=True)
    fecha = fields.Date(string="Date")

    _order = 'id_comprador, fecha'

    @api.constrains('id_inventario','cantidad')
    def _check_stock_is_enough(self):
        print("FUNCTION _check_stock_is_enough RUNNING (Compra)")
        stock = self.id_inventario.cantidad
        producto = self.id_inventario.name
        cantidad = self.cantidad
        mensaje = None
        if cantidad >= 0:
            if  stock < 0:
                mensaje = "\tThere is not stock from " + str(producto)
                print(mensaje)
                raise ValidationError(mensaje)
            else:
                mensaje = "\tStock of " + str(producto) + " exists"
                print(mensaje)
                if stock < cantidad:
                    mensaje = "\tNot enough stock: " + str(stock) + "(Stock) vs " + str(cantidad)+"(Cantidad)"
                    print(mensaje)
                    raise ValidationError(mensaje)
                else:
                    mensaje = "\tEnough stock: " + str(stock) + "(Stock) vs " + str(cantidad)+"(Cantidad)"
                    print(mensaje)
                    self._descontar_cantidad_inventario()
        else:
            mensaje = "\tYou can't buy" + str(cantidad) + "(Unids)"
            print(mensaje)
            raise ValidationError(mensaje)

    def name_get(self):
        print("FUNCTION name_get RUNNING (Compra)")
        result = []
        for compra in self:
            name = compra.id_inventario.name + " " + compra.id_comprador.name
            print("\t" + name)
            result.append((compra.id, name))
        return result

    def _descontar_cantidad_inventario(self):
        print("FUNCTION _descontar_cantidad_inventario RUNNING (Compra)")

        cantidadInventarioSinDescontar = self.id_inventario.cantidad
        cantidadCompra = self.cantidad
        print("\tcantidadInventarioSinDescontar: " + str(cantidadInventarioSinDescontar))
        print("\tcantidadCompra: " + str(cantidadCompra))

        self.id_inventario.cantidad = cantidadInventarioSinDescontar - cantidadCompra
        print("\tcantidadInventarioDescontado: " + str(cantidadInventarioSinDescontar - cantidadCompra))