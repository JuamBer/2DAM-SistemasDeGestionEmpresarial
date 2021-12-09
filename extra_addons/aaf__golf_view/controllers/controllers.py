# -*- coding: utf-8 -*-
# from odoo import http


# class AafGolfView(http.Controller):
#     @http.route('/aaf__golf_view/aaf__golf_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aaf__golf_view/aaf__golf_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aaf__golf_view.listing', {
#             'root': '/aaf__golf_view/aaf__golf_view',
#             'objects': http.request.env['aaf__golf_view.aaf__golf_view'].search([]),
#         })

#     @http.route('/aaf__golf_view/aaf__golf_view/objects/<model("aaf__golf_view.aaf__golf_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aaf__golf_view.object', {
#             'object': obj
#         })
