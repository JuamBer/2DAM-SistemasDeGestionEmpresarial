# -*- coding: utf-8 -*-
# from odoo import http


# class AaeGolf(http.Controller):
#     @http.route('/aae__golf/aae__golf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aae__golf/aae__golf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aae__golf.listing', {
#             'root': '/aae__golf/aae__golf',
#             'objects': http.request.env['aae__golf.aae__golf'].search([]),
#         })

#     @http.route('/aae__golf/aae__golf/objects/<model("aae__golf.aae__golf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aae__golf.object', {
#             'object': obj
#         })
