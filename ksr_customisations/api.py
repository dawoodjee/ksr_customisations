import frappe
from hijri_converter import convert
import datetime
from datetime import datetime


@frappe.whitelist()
def get_hijry_today():
	datee = datetime.datetime.strptime(frappe.utils.today(), "%Y-%m-%d")
	d = convert.Gregorian(datee.year, datee.month, datee.day).to_hijri()
	d = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2)
	frappe.errprint(d)
	return str(d)

	# ksr_customisations/ksr_customisations/ksrnr_customisations/report/government_salary_pdf/government_salary_pdf.py
	# frappe/custom/doctype/custom_field/custom_field.py


@frappe.whitelist()
def to_hijry(greg):
	datee = datetime.strptime(greg, "%Y-%m-%d")
	d = convert.Gregorian(datee.year, datee.month, datee.day).to_hijri()
	return str(d)

def set_employee_number(employee, method):
	employee.db_set("employee_number", str(employee.name)[-4:])

def convert_date(employee, method):
	pass
	if employee.date_of_birth != None:
		birth_date = datetime.strptime(str(employee.date_of_birth), "%Y-%m-%d")
		d = convert.Gregorian(birth_date.year, birth_date.month, birth_date.day).to_hijri()
		hb = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2)
		employee.db_set('date_of_birth_hijri', hb)
	
	if employee.agency_employment_date != None:
		employement_date = datetime.strptime(str(employee.agency_employment_date), "%Y-%m-%d")
		d = convert.Gregorian(employement_date.year, employement_date.month, employement_date.day).to_hijri()
		hb = str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(2)
		employee.db_set('agency_employment_date_hijri', hb)
		
	if employee.date_of_joining != None:
		join_date = datetime.strptime(str(employee.date_of_joining), "%Y-%m-%d")
		d = convert.Gregorian(join_date.year, join_date.month, join_date.day).to_hijri()
		hb = str(d.year) + "/" + str(d.month).zfill(2) + "/" + str(d.day).zfill(2)
		employee.db_set('gov_employment_date_hijri', hb)