# -*- coding: utf-8 -*-
# from odoo import http


# class AacBibloteca(http.Controller):
#     @http.route('/aac__bibloteca/aac__bibloteca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aac__bibloteca/aac__bibloteca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aac__bibloteca.listing', {
#             'root': '/aac__bibloteca/aac__bibloteca',
#             'objects': http.request.env['aac__bibloteca.aac__bibloteca'].search([]),
#         })

#     @http.route('/aac__bibloteca/aac__bibloteca/objects/<model("aac__bibloteca.aac__bibloteca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aac__bibloteca.object', {
#             'object': obj
#         })
