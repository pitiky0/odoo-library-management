/** @odoo-module */

import { registry } from "@web/core/registry";
import { StandardField } from "@web/views/fields/standard_field";
import { Component, xml } from "@odoo/owl";

// كنعرفو الكومبوننت ديالنا
export class StarRating extends StandardField {
    // الدالة اللي كتنفذ فاش كنكليكيو على نجمة
    // value هو رقم النجمة (1, 2, 3...)
    setRating(value) {
        // props.record.update هي الطريقة باش كنبدلو القيمة فالداتابيز عبر OWL
        this.props.record.update({ [this.props.name]: value });
    }
}

// هنا كنربطو الكود بالتمبليت (XML) اللي غنصاوبو دابا
StarRating.template = "library_app.StarRating";

// كنسجلو الويجت فـ Odoo باش نقدرو نستعملوه فـ XML Views
export const starRatingField = {
    component: StarRating,
    supportedTypes: ["integer"], // كيخدم غير مع الأرقام
};

registry.category("fields").add("star_rating", starRatingField);