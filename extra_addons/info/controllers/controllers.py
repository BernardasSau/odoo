# -*- coding: utf-8 -*-
# from odoo import http


# class Info(http.Controller):
#     @http.route('/info/info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/info/info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('info.listing', {
#             'root': '/info/info',
#             'objects': http.request.env['info.info'].search([]),
#         })

#     @http.route('/info/info/objects/<model("info.info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('info.object', {
#             'object': obj
#         })
