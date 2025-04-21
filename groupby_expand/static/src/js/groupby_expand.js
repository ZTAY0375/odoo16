// /** @odoo-module */
// import { ListController } from "@web/views/list/list_controller";

// // Add the click handler for the button
// ListController.prototype.onClickExpandButton = async function () {
//   await this.expandAllGroups();
// };

// // Expand all top-level groups
// ListController.prototype.expandAllGroups = async function () {
//   const allGroups = this.model.root.groups;
//   for (let i = 0; i < allGroups.length; i++) {
//     await this.expand(allGroups[i]);
//   }
// };

// // Recursively expand each group and its children
// ListController.prototype.expand = async function (group) {
//   if (group.isFolded) {
//     await group.toggle();
//   }};





// /** @odoo-module **/

// import { ListController } from "@web/views/list/list_controller";
// import { patch } from "@web/core/utils/patch";
// import { useService } from "@web/core/utils/hooks";

// patch(ListController.prototype, "custom_expand_groups_button", {
//     setup() {
//         this._super.apply(this, arguments);

//         // Initialize notification service
//         this.notification = useService("notification");
//     },

//     async onClickExpandButton() {
//         const groupBy = this.model?.root?.groupBy || [];
//         const allGroups = this.model?.root?.groups || [];

//         if (groupBy.length === 0 || allGroups.length === 0) {
//             this.notification.add("The current view isn't grouped.", {
//                 type: "warning",
//                 title: "Grouping Required",
//             });
//             return;
//         }

//         for (let i = 0; i < allGroups.length; i++) {
//             await this.expand(allGroups[i]);
//         }

//         this.notification.add(`Expanded ${allGroups.length} group(s).`, {
//             type: "success",
//             title: "Done",
//         });
//     },

//     async expand(group) {
//         if (group.isFolded) {
//             await group.toggle();
//         }
//     },
// });

/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(ListController.prototype, "custom_expand_groups_button", {
    setup() {
        this._super.apply(this, arguments);

        // Initialize notification service
        this.notification = useService("notification");
    },

    async onClickExpandButton() {
        const groupBy = this.model?.root?.groupBy || [];
        const allGroups = this.model?.root?.groups || [];

        if (groupBy.length === 0 || allGroups.length === 0) {
            this.notification.add("The current view isn't grouped.", {
                type: "warning",
                title: "Grouping Required",
            });
            return;
        }

        for (let i = 0; i < allGroups.length; i++) {
            await this.expand(allGroups[i]);
        }

        this.notification.add(`Expanded ${allGroups.length} group(s).`, {
            type: "success",
            title: "Done",
        });
    },

    async expand(group) {
        if (group.isFolded) {
            await group.toggle();
        }
    },
});
