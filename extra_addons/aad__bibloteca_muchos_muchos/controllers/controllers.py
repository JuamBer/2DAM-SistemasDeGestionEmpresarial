# -*- coding: utf-8 -*-
# from odoo import http


# class AadBiblotecaMuchosMuchos(http.Controller):
#     @http.route('/aad__bibloteca_muchos_muchos/aad__bibloteca_muchos_muchos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aad__bibloteca_muchos_muchos/aad__bibloteca_muchos_muchos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aad__bibloteca_muchos_muchos.listing', {
#             'root': '/aad__bibloteca_muchos_muchos/aad__bibloteca_muchos_muchos',
#             'objects': http.request.env['aad__bibloteca_muchos_muchos.aad__bibloteca_muchos_muchos'].search([]),
#         })

#     @http.route('/aad__bibloteca_muchos_muchos/aad__bibloteca_muchos_muchos/objects/<model("aad__bibloteca_muchos_muchos.aad__bibloteca_muchos_muchos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aad__bibloteca_muchos_muchos.object', {
#             'object': obj
#         })
