#-*- coding: utf-8 -*-

from odoo import models, fields, api


class modulo1_modelo(models.Model):
    _name = 'modulo1.modulo'
    _description = 'modulo inicial de ejemplo'

    name = fields.Char(string="Nombre", required=True)
    value = fields.Integer(string="Edad")

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
