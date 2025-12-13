frappe.ui.form.on("Sales Invoice", {
    onload: function (frm) {

        // Do nothing for Administrator
        if (frappe.session.user === "Administrator") return;

        // Step 1: Get Retail Store from User (only if not already set)
        if (!frm.doc.custom_retail_store) {
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "User",
                    filters: { name: frappe.session.user },
                    fieldname: "retail_store"
                },
                callback: function (r) {
                    if (r.message && r.message.retail_store) {
                        frm.set_value("custom_retail_store", r.message.retail_store);

                        // Step 2: Get Cost Center from Retail Store
                        fetch_cost_center(frm, r.message.retail_store);
                    }
                }
            });
        }
        // If Retail Store already exists, just fetch Cost Center
        else if (!frm.doc.cost_center) {
            fetch_cost_center(frm, frm.doc.custom_retail_store);
        }
    }
});

// Helper function
function fetch_cost_center(frm, retail_store) {
    frappe.call({
        method: "frappe.client.get_value",
        args: {
            doctype: "Retail Store",
            filters: { name: retail_store },
            fieldname: "cost_center"
        },
        callback: function (r) {
            if (r.message && r.message.cost_center) {
                frm.set_value("cost_center", r.message.cost_center);
            }
        }
    });
}
