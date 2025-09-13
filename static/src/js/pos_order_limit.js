odoo.define('pos_order_limit.TicketScreenLimit', function (require) {
    'use strict';

    const TicketScreen = require('point_of_sale.TicketScreen');
    const Registries = require('point_of_sale.Registries');

    const TicketScreenLimit = (TicketScreen) =>
        class extends TicketScreen {
            async _onCreateNewOrder() {
                const config = this.env.pos.config;
                const pendingLimit = config.enable_pending_order_limit ? config.pending_orders_limit || 0 : 0;

                const pendingOrders = this.env.pos.get_order_list().filter(order =>
                    (order.is_to_invoice() || order.get_orderlines().length > 0) && !order.finalized
                );

                if (pendingLimit > 0 && pendingOrders.length >= pendingLimit) {
                    await this.showPopup('ErrorPopup', {
                        title: 'Limite atteinte',
                        body: `Impossible de créer une nouvelle commande : vous avez atteint la limite de ${pendingLimit} commandes en attente. Veuillez Supprimer ou procéder au paiement des commandes anterieures`,
                    });
                    return;
                }

                this.env.pos.add_new_order();
                this.showScreen('ProductScreen');
            }
        };

    Registries.Component.extend(TicketScreen, TicketScreenLimit);

    return TicketScreenLimit;
});