# Copyright (c) 2025, man and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class ServiceRequest(Document):

	def validate(self):
		self.automate_fields()

def automate_fields(self):
    if not self.request_date:
        self.request_date = nowdate()

    if not self.tasks:
        frappe.throw("At least one task is needed")

    has_open_task = False

    for task in self.tasks:
        if not task.task_description:
            frappe.throw("Give task description")

        if not task.status:
            frappe.throw("Status should be selected")

        if task.status == "Open":
            has_open_task = True

    total_tasks = len(self.tasks)
    open_tasks = 0
    done_tasks = 0

    for task in self.tasks:
        if task.status == "Open":
            open_tasks += 1
        elif task.status == "Done":
            done_tasks += 1


    if has_open_task:
        self.status = "In Progress"
    else:
        self.status = "Completed"

    if self.status == "In Progress":
        self.priority = "High"
    else:
        self.priority = "Low"

    if self.status == "Completed":
        self.assigned_to = None

    if self.status == "Cancelled":
        self.priority = None
        self.assigned_to = None
