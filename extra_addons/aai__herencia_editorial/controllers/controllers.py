# -*- coding: utf-8 -*-
# from odoo import http


# class AaiHerenciaEditorial(http.Controller):
#     @http.route('/aai__herencia_editorial/aai__herencia_editorial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aai__herencia_editorial/aai__herencia_editorial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aai__herencia_editorial.listing', {
#             'root': '/aai__herencia_editorial/aai__herencia_editorial',
#             'objects': http.request.env['aai__herencia_editorial.aai__herencia_editorial'].search([]),
#         })

#     @http.route('/aai__herencia_editorial/aai__herencia_editorial/objects/<model("aai__herencia_editorial.aai__herencia_editorial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aai__herencia_editorial.object', {
#             'object': obj
#         })
