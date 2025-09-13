from odoo import models, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create_from_ui(self, orders, draft=False):
        _logger.warning("=== create_from_ui CALLED ===")
        for order_data in orders:
            if draft and 'pos_session_id' in order_data:
                session = self.env['pos.session'].browse(order_data['pos_session_id'])
                _logger.warning(f"Session: {session}, Config: {session.config_id}, Limit: {session.config_id.pending_orders_limit}")
                if session and session.config_id:
                    result = session.check_pending_orders_limit(session.config_id.id)
                    _logger.warning(f"Result: {result}")
                    if not result['success']:
                        raise UserError(result['message'])
        return super().create_from_ui(orders, draft)