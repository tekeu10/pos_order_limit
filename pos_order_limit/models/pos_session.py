from odoo import models, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    @api.model
    def check_pending_orders_limit(self, config_id):
        config = self.env['pos.config'].browse(config_id)
        if not config or not config.pending_orders_limit:
            return {'success': True, 'current_count': 0, 'max_count': 0, 'message': ''}
        count = self.env['pos.order'].search_count([
            ('session_id.config_id', '=', config_id),
            ('state', '=', 'draft')
        ])
        if count >= config.pending_orders_limit:
            return {
                'success': False,
                'current_count': count,
                'max_count': config.pending_orders_limit,
                'message': f"Limite de {config.pending_orders_limit} commandes en attente atteinte."
            }
        return {
            'success': True,
            'current_count': count,
            'max_count': config.pending_orders_limit,
            'message': ''
        }