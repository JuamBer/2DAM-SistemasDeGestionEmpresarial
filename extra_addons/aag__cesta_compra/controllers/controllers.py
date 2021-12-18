# -*- coding: utf-8 -*-
# from odoo import http


# class AagCestaCompra(http.Controller):
#     @http.route('/aag__cesta_compra/aag__cesta_compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aag__cesta_compra/aag__cesta_compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aag__cesta_compra.listing', {
#             'root': '/aag__cesta_compra/aag__cesta_compra',
#             'objects': http.request.env['aag__cesta_compra.aag__cesta_compra'].search([]),
#         })

#     @http.route('/aag__cesta_compra/aag__cesta_compra/objects/<model("aag__cesta_compra.aag__cesta_compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aag__cesta_compra.object', {
#             'object': obj
#         })
