# Copyright (c) 2025, man and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class ServiceRequest(Document):
	def validate(self):
		if not self.request_date:
			self.request_date = nowdate()


