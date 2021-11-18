# -*- coding: utf-8 -*-
# from odoo import http


# class AabAutor(http.Controller):
#     @http.route('/aab__autor/aab__autor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aab__autor/aab__autor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aab__autor.listing', {
#             'root': '/aab__autor/aab__autor',
#             'objects': http.request.env['aab__autor.aab__autor'].search([]),
#         })

#     @http.route('/aab__autor/aab__autor/objects/<model("aab__autor.aab__autor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aab__autor.object', {
#             'object': obj
#         })
