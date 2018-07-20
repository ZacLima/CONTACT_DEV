# -*- coding: utf-8 -*-

from odoo import models, fields

class InvitadoInvited(models.Model):
    _inherit = 'helpdesk.tag'
    invited_ids = fields.Many2many('res.partner', string='Seguidores', ondelete='cascade')
