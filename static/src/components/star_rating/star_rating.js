/** @odoo-module */

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class StarRating extends Component {
    static template = "library_app.StarRating";
    static props = {
        ...standardFieldProps, // كنورثو الخصائص القياسية ديال الحقول
    };

    setRating(value) {
        // كنبدلو القيمة فالداتابيز
        this.props.record.update({ [this.props.name]: value });
    }
}

export const starRatingField = {
    component: StarRating,
    supportedTypes: ["integer"],
};

registry.category("fields").add("star_rating", starRatingField);