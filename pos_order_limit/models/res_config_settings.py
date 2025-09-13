# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_max_pending_orders = fields.Integer(
        related='pos_config_id.max_pending_orders',
        string="Limite commandes en attente",
        readonly=False,
        store=True
    )
    pos_block_pending_orders = fields.Boolean(
        related='pos_config_id.block_pending_orders',
        string="Bloquer les commandes en attente",
        readonly=False,
        store=True
    )