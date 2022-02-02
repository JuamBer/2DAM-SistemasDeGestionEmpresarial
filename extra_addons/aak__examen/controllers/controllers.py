# -*- coding: utf-8 -*-
# from odoo import http


# class AakExamen(http.Controller):
#     @http.route('/aak__examen/aak__examen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aak__examen/aak__examen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aak__examen.listing', {
#             'root': '/aak__examen/aak__examen',
#             'objects': http.request.env['aak__examen.aak__examen'].search([]),
#         })

#     @http.route('/aak__examen/aak__examen/objects/<model("aak__examen.aak__examen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aak__examen.object', {
#             'object': obj
#         })
