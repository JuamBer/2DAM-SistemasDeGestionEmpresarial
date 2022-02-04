# -*- coding: utf-8 -*-
# from odoo import http


# class Saez(http.Controller):
#     @http.route('/saez/saez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saez/saez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saez.listing', {
#             'root': '/saez/saez',
#             'objects': http.request.env['saez.saez'].search([]),
#         })

#     @http.route('/saez/saez/objects/<model("saez.saez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saez.object', {
#             'object': obj
#         })
