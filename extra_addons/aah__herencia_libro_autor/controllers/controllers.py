# -*- coding: utf-8 -*-
# from odoo import http


# class AahHerenciaLibroAutor(http.Controller):
#     @http.route('/aah__herencia_libro_autor/aah__herencia_libro_autor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aah__herencia_libro_autor/aah__herencia_libro_autor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aah__herencia_libro_autor.listing', {
#             'root': '/aah__herencia_libro_autor/aah__herencia_libro_autor',
#             'objects': http.request.env['aah__herencia_libro_autor.aah__herencia_libro_autor'].search([]),
#         })

#     @http.route('/aah__herencia_libro_autor/aah__herencia_libro_autor/objects/<model("aah__herencia_libro_autor.aah__herencia_libro_autor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aah__herencia_libro_autor.object', {
#             'object': obj
#         })
