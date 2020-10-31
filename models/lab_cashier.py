# -*- coding: utf-8 -*-
from odoo import fields, models, api

class cashier(models.Model):
    _inherit = 'hr.employee'
    nationality = fields.Char()


