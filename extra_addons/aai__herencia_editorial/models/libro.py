from odoo import models, fields, api

class libro(models.Model):
    _inherit = 'aah_herencia_libro_autor.libro'
    editorial_id = fields.Many2one('aai_herencia_editorial.editorial', string='Editorial')