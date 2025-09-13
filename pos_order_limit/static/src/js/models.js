/** @odoo-module **/

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    async setup() {
        await super.setup(...arguments);
        
        // Initialiser les paramètres de limite de commandes depuis la configuration chargée
        const configParams = this.config_parameter_data || {};
        this.orderLimitEnabled = configParams['pos_order_limit.enable_order_limit'] === 'True';
        this.maxOpenedOrders = parseInt(configParams['pos_order_limit.max_opened_orders'] || '5');
    },

    getOpenedOrdersCount() {
        // Compter les commandes qui ont des lignes de commande (ne sont pas vides)
        return this.orders.filter(order => 
            order.get_orderlines && order.get_orderlines().length > 0
        ).length;
    },

    canCreateNewOrder() {
        if (!this.orderLimitEnabled || this.maxOpenedOrders === 0) {
            return true; // Illimité ou désactivé
        }
        const openedCount = this.getOpenedOrdersCount();
        return openedCount < this.maxOpenedOrders;
    },

    getOrdersLimitMessage() {
        const openedCount = this.getOpenedOrdersCount();
        return `Vous avez atteint la limite maximale de commandes ouvertes (${openedCount}/${this.maxOpenedOrders}). Veuillez compléter ou supprimer quelques commandes avant d'en créer de nouvelles.`;
    },

    async addNewOrder() {
        if (!this.canCreateNewOrder()) {
            await this.env.services.popup.add("ConfirmPopup", {
                title: 'Limite de Commandes Ouvertes',
                body: this.getOrdersLimitMessage(),
                confirmText: 'Ok',
                cancelText: '',
            });
            return null;
        }
        return super.addNewOrder();
    }
});