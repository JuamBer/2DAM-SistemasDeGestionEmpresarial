# -*- coding: utf-8 -*-
# from odoo import http


# class AajDemoData(http.Controller):
#     @http.route('/aaj__demo_data/aaj__demo_data/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aaj__demo_data/aaj__demo_data/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aaj__demo_data.listing', {
#             'root': '/aaj__demo_data/aaj__demo_data',
#             'objects': http.request.env['aaj__demo_data.aaj__demo_data'].search([]),
#         })

#     @http.route('/aaj__demo_data/aaj__demo_data/objects/<model("aaj__demo_data.aaj__demo_data"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aaj__demo_data.object', {
#             'object': obj
#         })
