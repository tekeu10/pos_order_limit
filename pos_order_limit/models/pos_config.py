from odoo import models, fields, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_pending_order_limit = fields.Boolean(
        string="Enable Order Limitation",
        default=False,
        help="Enable checking the number of pending orders in POS."
    )

    pending_orders_limit = fields.Integer(
        string="Pending Orders Limit",
        default=3,
        help="Maximum number of pending orders allowed."
    )

    @api.model
    def _get_pos_ui_fields(self):
        fields = super()._get_pos_ui_fields()
        fields.extend([
            'enable_pending_order_limit',
            'pending_orders_limit',
        ])
        return fields