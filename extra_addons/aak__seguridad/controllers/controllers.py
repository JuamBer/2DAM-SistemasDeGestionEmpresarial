# -*- coding: utf-8 -*-
# from odoo import http


# class AakSeguridad(http.Controller):
#     @http.route('/aak__seguridad/aak__seguridad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aak__seguridad/aak__seguridad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aak__seguridad.listing', {
#             'root': '/aak__seguridad/aak__seguridad',
#             'objects': http.request.env['aak__seguridad.aak__seguridad'].search([]),
#         })

#     @http.route('/aak__seguridad/aak__seguridad/objects/<model("aak__seguridad.aak__seguridad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aak__seguridad.object', {
#             'object': obj
#         })
