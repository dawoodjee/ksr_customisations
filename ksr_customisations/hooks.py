from . import __version__ as app_version

app_name = "ksr_customisations"
app_title = "KSRNR Customisations"
app_publisher = "Bantoo"
app_description = "KSRNR Customisations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "devs@thebantoo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#app_include_css = "/assets/ksr_customisations/css/ksr_customisations.css"
# app_include_js = "/assets/ksr_customisations/js/ksr_customisations.js"

# include js, css files in header of web template
web_include_css = "/assets/ksr_customisations/css/ksr_customisations.css"
# web_include_js = "/assets/ksr_customisations/js/ksr_customisations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ksr_customisations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ksr_customisations.install.before_install"
# after_install = "ksr_customisations.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ksr_customisations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Employee": {
			"validate": "ksr_customisations.api.convert_date",
			"on_update": "ksr_customisations.api.set_employee_number",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ksr_customisations.tasks.all"
# 	],
# 	"daily": [
# 		"ksr_customisations.tasks.daily"
# 	],
# 	"hourly": [
# 		"ksr_customisations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ksr_customisations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ksr_customisations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ksr_customisations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ksr_customisations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ksr_customisations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

"""
jenv = {
	"methods": [
		"get_hijri_today:ksr_customisations.ksr_customisations.api.get_hijry_today"
	]
}"""

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ksr_customisations.auth.validate"
# ]


fixtures = [
	{
		"dt": "Bank Code",
		"filters": [],
	},
    {
		"dt": "Client Script",
		"filters": [
			[
                "name", "in", [
					"Journal Entry-Form"                    
                ]
            ]
        ],
	},
	{
		"dt": "Custom Field",
		"filters": [
			[
				"name", "in", [
					"Employee-occupation_classification",
					"Employee-nationality"
					"Employee-employee_job_title",
					"Employee-supplementary_payment",
					"Employee-full_name_english",
					"Employee-emp_job_grade",
					"Employee-emp_job_rank",
					"Employee-agency_employment_date_hijri",
					"Employee-agency_employment_date",
					"Employee-txdtls",
					"Employee-acctnum",
					"Employee-bank_code",
					"Employee-empjobclass",
					"Employee-jobnumber",
					"Employee-date_of_joining",
					"Employee-gov_employment_date_hijri",
					"Employee-date_of_birth_hijri",
					"Employee-nin",
					"Employee-number",
					"Employee-passport",
					"Salary Slip-birth_date_hijri",
					"Salary Slip-birth_date",
					"Salary Slip-government_employment_date",
					"Salary Slip-agency_employment_date_hijri",
					"Salary Slip-agency_employment_date",
					"Salary Slip-occupation_classification",
					"Salary Slip-passport",
					"Salary Slip-nin",
					"Salary Slip-full_name_ar",
					"Salary Slip-gender",
					"Salary Slip-nationality",
					"Salary Slip-marital_status",
					"Salary Slip-column_break_96",
					"Salary Slip-employee_number",
					"Salary Slip-job_number",
					"Salary Slip-employee_job_title",
					"Salary Slip-employee_job_class",
					"Salary Slip-employee_job_rank",
					"Salary Slip-employee_job_grade",
					"Salary Slip-column_break_86",
					"Salary Slip-bank_code",
					"Salary Slip-account_number",
					"Salary Slip-txdtls",
					"Salary Slip-custom_fields"

				]
			]
		]
	},
]
