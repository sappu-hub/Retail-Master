import frappe
def validate_selling(doc,method = None):
	for item in doc.items:
		if item.rate<= item.incoming_rate:
			frappe.throw(f" !!!!selling rate lesser than {item.item_code}")