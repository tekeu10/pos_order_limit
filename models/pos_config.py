from odoo import models, fields, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_pending_order_limit = fields.Boolean(
        string="Activer la limitation des commandes",
        default=False,
        help="Active la vérification du nombre de commandes en attente dans le POS."
    )

    pending_orders_limit = fields.Integer(
        string="Limite de commandes en attente",
        default=3,
        help="Nombre maximum de commandes en attente autorisées."
    )

    @api.model
    def _get_pos_ui_fields(self):
        fields = super()._get_pos_ui_fields()
        fields.extend([
            'enable_pending_order_limit',
            'pending_orders_limit',
        ])
        return fields