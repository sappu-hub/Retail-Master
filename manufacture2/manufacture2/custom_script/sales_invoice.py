import frappe
def validate_selling(doc,method = None):
	for item in doc.items:
		if item.rate<= item.incoming_rate:
			frappe.throw(f" !!!!selling rate lesser than {item.item_code}")

def apply_store_warehouse(doc,method=None):
	
	if not doc.custom_retail_store:
		return
	
	store = frappe.get_doc("Retail Store",doc.custom_retail_store)

	if not store.default_warehouse:
		frappe.throw("Warehouse Need to Be selected")

	default_warehouse = store.default_warehouse

	for item in doc.items:
		item.warehouse = default_warehouse