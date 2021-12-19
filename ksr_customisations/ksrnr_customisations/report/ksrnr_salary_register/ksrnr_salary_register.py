# Copyright (c) 2013, Bantoo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt
from frappe import _
from datetime import datetime # from python std library

def format_date(d):
	if d:
		formatted_date = datetime.strptime(str(d), "%Y-%m-%d")
		return formatted_date.strftime("%Y%m%d")

def execute(filters=None):
	if not filters: filters = {}
	currency = None
	if filters.get('currency'):
		currency = filters.get('currency')
	company_currency = erpnext.get_company_currency(filters.get("company"))
	salary_slips = get_salary_slips(filters, company_currency)
	if not salary_slips: return [], []

	columns, earning_types, ded_types = get_columns(salary_slips)
	ss_earning_map = get_ss_earning_map(salary_slips, currency, company_currency)
	ss_ded_map = get_ss_ded_map(salary_slips,currency, company_currency)

	data = []
	count = 1

	for ss in salary_slips:
			
		gender = "M" if ss.gender == "Male"	else "F"

		row = []

		# deductions

		d5000gosi = ss_ded_map.get(ss.name, {}).get("حسم المؤسسة العامة للتأمينات الاجتماعية") if ss_ded_map.get(ss.name, {}).get("حسم المؤسسة العامة للتأمينات الاجتماعية") else 0
		d5002 = ss_ded_map.get(ss.name, {}).get("حسم صندوق التنمية العقارية") if ss_ded_map.get(ss.name, {}).get("حسم صندوق التنمية العقارية") else 0
		d5003 = ss_ded_map.get(ss.name, {}).get("حسم بنك التنمية الاجتماعية") if ss_ded_map.get(ss.name, {}).get("حسم بنك التنمية الاجتماعية") else 0
		d5004 = ss_ded_map.get(ss.name, {}).get("حسم صندوق التنمية الزراعية") if ss_ded_map.get(ss.name, {}).get("حسم صندوق التنمية الزراعية") else 0
		d5005 = ss_ded_map.get(ss.name, {}).get("حسم لصالح الجهة نفسها") if ss_ded_map.get(ss.name, {}).get("حسم لصالح الجهة نفسها") else 0

		# earnings
		e1031 = ss_ded_map.get(ss.name, {}).get("بدل سكن") if ss_ded_map.get(ss.name, {}).get("بدل سكن") else 0
		e1053 = ss_ded_map.get(ss.name, {}).get("بدل ندرة") if ss_ded_map.get(ss.name, {}).get("بدل ندرة") else 0
		e1083 = ss_ded_map.get(ss.name, {}).get("بدل المواصلات") if ss_ded_map.get(ss.name, {}).get("بدل المواصلات") else 0
		basic = ss_ded_map.get(ss.name, {}).get("الراتب الأساسي")
		
		if currency == company_currency:
			row += [flt(ss.net_pay) * flt(ss.exchange_rate), flt(ss.total_deduction) * flt(ss.exchange_rate)]
		else:
			row += [ss.net_pay, ss.total_deduction]

		row.append(d5005)
		row.append(d5004)
		row.append(d5003)
		row.append(d5002)
		row.append(d5000gosi)

		if currency == company_currency:
			row += [flt(ss.gross_pay) * flt(ss.exchange_rate)]
		else:
			row += [ss.gross_pay]

		row.append(e1031)
		row.append(e1053)
		row.append(e1083)
		row.append(basic)
		row.extend([
			basic, ss.account_number, ss.bank_code, ss.employee_job_grade, ss.employee_job_rank, ss.occupation_classification, 
			ss.employee_job_title, ss.job_number, format_date(ss.agency_employment_date), ss.agency_employment_date_hijri,
			format_date(ss.government_employment_date), ss.government_employment_date_hijri, ss.marital_status, ss.employee_number,
			ss.nationality, gender, format_date(ss.birth_date), ss.birth_date_hijri, ss.full_name_ar, ss.nin, count			
		])
		data.append(list(reversed(row)))
		count += 1
	#add second row for title
	data.insert(0, list(reversed([
		"الصافي", "إجمالي الاستقطاعات", "حسم لصالح الجهة نفسها", "حسم صندوق التنمية الزراعية", "حسم بنك التنمية الاجتماعية", "حسم صندوق التنمية العقارية", "حسم المؤسسة العامة للتأمينات الاجتماعية", "إجمالي الاستحقاقات", "بدل المواصلات", "بدل ندرة", "بدل سكن", "الراتب الأساسي", "الراتب الأساسي الفعلي", "رقم الحساب البنكي الآيبان", "رمز البنك", "الدرجة", "المرتبة", "الكادر", "المسمى الوظيفي", "رقم الوظيفة", "تاريخ التعيين في الجهة الحكومية ميلادي", "تاريخ التعيين في الجهة الحكومية هجري", "تاريخ التعيين بالحكومة ميلادي", "تاريخ التعيين بالحكومة هجري", "رقم الموظف الوظيفي", "الحالة الاجتماعية", "الجنسية", "الجنس", "تاريخ الميلاد ميلادي", "تاريخ الميلاد هجري", "اسم الموظف الرباعي بالعربي", "رقم الهوية / الإقامة للموظف", "الرقم التسلسلي"
	])))

	return list(reversed(columns)), data

def get_columns(salary_slips):

	columns = [
		"NetAmt", "TotalDeductions", "5005", "5004", "5003", "5002", "5000",
		"TotalAllowances", "1083", "1053", "1031", "BasicSalary",
		"TxDtls", "AcctNum", "BankCode", "EmpJobGrade", "EmpJobRank", "EmpJobClass", "EmpJobTitle",
		"JobNumber", "AgencyEmploymentDt", "AgencyEmploymentDtHjr", "GovEmploymentDt", "GovEmploymentDtHjr", 
		"EmployeeNumber", "MaritalStatus", "Nationality", "Gender", "BirthDt", "BirthDtHjr", "FullNameAr", "NIN", "SerialNo"
	]

	salary_components = {_("Earning"): [], _("Deduction"): []}

	for component in frappe.db.sql("""select distinct sd.salary_component, sc.type
		from `tabSalary Detail` sd, `tabSalary Component` sc
		where sc.name=sd.salary_component and sd.amount != 0 and sd.parent in (%s)""" %
		(', '.join(['%s']*len(salary_slips))), tuple([d.name for d in salary_slips]), as_dict=1):
		salary_components[_(component.type)].append(component.salary_component)

	return columns, salary_components[_("Earning")], salary_components[_("Deduction")]

def get_salary_slips(filters, company_currency):
	filters.update({"from_date": filters.get("from_date"), "to_date":filters.get("to_date")})
	conditions, filters = get_conditions(filters, company_currency)
	salary_slips = frappe.db.sql("""select * from `tabSalary Slip` where %s
		order by employee""" % conditions, filters, as_dict=1)

	return salary_slips or []

def get_conditions(filters, company_currency):
	conditions = ""
	doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}

	if filters.get("docstatus"):
		conditions += "docstatus = {0}".format(doc_status[filters.get("docstatus")])

	if filters.get("from_date"): conditions += " and start_date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and end_date <= %(to_date)s"
	if filters.get("company"): conditions += " and company = %(company)s"
	if filters.get("employee"): conditions += " and employee = %(employee)s"
	if filters.get("currency") and filters.get("currency") != company_currency:
		conditions += " and currency = %(currency)s"

	return conditions, filters

def get_employee_doj_map():
	return	frappe._dict(frappe.db.sql("""
				SELECT
					employee,
					date_of_joining
				FROM `tabEmployee`
				"""))

def get_ss_earning_map(salary_slips, currency, company_currency):
	ss_earnings = frappe.db.sql("""select sd.parent, sd.salary_component, sd.amount, ss.exchange_rate, ss.name
		from `tabSalary Detail` sd, `tabSalary Slip` ss where sd.parent=ss.name and sd.parent in (%s)""" % 
		(', '.join(['%s']*len(salary_slips))), tuple([d.name for d in salary_slips]), as_dict=1)

	ss_earning_map = {}
	for d in ss_earnings:
		
		ss_earning_map.setdefault(d.parent, frappe._dict()).setdefault(d.salary_component, [])
		if currency == company_currency:
			ss_earning_map[d.parent][d.salary_component] = flt(d.amount) * flt(d.exchange_rate if d.exchange_rate else 1)
		else:
			ss_earning_map[d.parent][d.salary_component] = flt(d.amount)

	return ss_earning_map

def get_ss_ded_map(salary_slips, currency, company_currency):
	ss_deductions = frappe.db.sql("""select sd.parent, sd.salary_component, sd.amount, ss.exchange_rate, ss.name
		from `tabSalary Detail` sd, `tabSalary Slip` ss where sd.parent=ss.name and sd.parent in (%s)""" %
		(', '.join(['%s']*len(salary_slips))), tuple([d.name for d in salary_slips]), as_dict=1)

	ss_ded_map = {}
	for d in ss_deductions:
		ss_ded_map.setdefault(d.parent, frappe._dict()).setdefault(d.salary_component, [])
		if currency == company_currency:
			ss_ded_map[d.parent][d.salary_component] = flt(d.amount) * flt(d.exchange_rate if d.exchange_rate else 1)
		else:
			ss_ded_map[d.parent][d.salary_component] = flt(d.amount)

	return ss_ded_map
