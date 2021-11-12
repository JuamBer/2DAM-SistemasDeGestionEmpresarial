# -*- coding: utf-8 -*-
# from odoo import http


# class AaaHolaMundo(http.Controller):
#     @http.route('/aaa__hola_mundo/aaa__hola_mundo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aaa__hola_mundo/aaa__hola_mundo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aaa__hola_mundo.listing', {
#             'root': '/aaa__hola_mundo/aaa__hola_mundo',
#             'objects': http.request.env['aaa__hola_mundo.aaa__hola_mundo'].search([]),
#         })

#     @http.route('/aaa__hola_mundo/aaa__hola_mundo/objects/<model("aaa__hola_mundo.aaa__hola_mundo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aaa__hola_mundo.object', {
#             'object': obj
#         })
