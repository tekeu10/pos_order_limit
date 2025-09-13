/** @odoo-module **/

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";

patch(ProductScreen.prototype, {
    _onClickNewOrder() {
        if (!this.pos.canCreateNewOrder()) {
            this.env.services.popup.add("ConfirmPopup", {
                title: 'Limite de Commandes Ouvertes',
                body: this.pos.getOrdersLimitMessage(),
                confirmText: 'Ok',
                cancelText: '',
            });
            return;
        }
        super._onClickNewOrder();
    }
});