""""Contains test data that are used as user inputs across various areasn in CCHQ"""
import os


class UserData:
    """User Test Data"""
    USER_INPUT_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Pre-setup application and case names
    village_application = "Village Health"
    reassign_cases_application = 'Reassign Cases'
    case_pregnancy = "pregnancy"
    case_reassign = "reassign"
    model_type_case = "case"
    model_type_form = "form"
    new_form_name = "Android Test Form"
    app_login = "appiumtest"
    app_password = "Pass@123"
    two_fa_user = "2fa.commcare.user@gmail.com"
    web_user = "[Web Users]"
    all_data = "[All Data]"
    mobile_testuser = "mobile_testuser"
    copied_to_user = "mobile_testuser \"DO NOT DELETE! DO NOT DELETE!\""
    searched_user = "appiumtest \"DO NOT DELETE! DO NOT DELETE!\""
    automation_group_users = ["appiumtest", "formplayer_user"]
    appiumtest_owner_id = "appiumtest@qa-automation.commcarehq.org"
    appiumtest_owner_id_prod = "appiumtest@qa-automation-prod.commcarehq.org"
    web_user = "automation.user.commcarehq@gmail.com"
    default_mw_role = "Mobile Worker Default"
    user_group = "automation_user"
    user_group_shared = "automation_user [case sharing]"
    assign_case_user = "mobile_testuser"
    view_by = ["Users", "Groups"]
    filter_dates_by = ["Completion Time", "Submission Time"]
    location = "updated_on"
    arrows_code = ['color: #8b0000', 'color: rgb(139, 0, 0)', 'color: #006400', 'color: rgb(0, 100, 0)']
    proj_perf_excel_tabs = ['Six Month Performance Summary', 'Inactive Users', 'Low Performing Users',
                            'New Performing Users']
    date_range = ["Last 7 Days", "Last Month", "Last 30 Days", "Custom Range"]
    wa_column_names = ["# Forms Submitted", "Avg # Forms Submitted", "Last Form Submission", "# Cases Created",
                       "# Cases Closed", "# Active Cases", "# Total Cases (Owned & Shared)", "% Active Cases"]
    wa_column_group_names = ["Form Data", "Case Data", "Case Activity"]

    ca_column_names = ["# Updated or Closed", "# Active", "# Closed"]
    ca_column_group_names = ["Cases in Last 30 Days", "Cases in Last 60 Days", "Cases in Last 90 Days"]

    fct_column_names = ["User", "Average", "Std. Dev.", "Shortest", "Longest", "No. of Forms"]
    fcst_column_names = ["User", "Completion Time", "Submission Time", "Form Name", "Difference"]

    sh_column_group_names = ["View Form", "Username", "Completion Time", "Form"]

    pagination = ['10', '25', '50', '100']
    # Phone Number
    area_code = "91"

    #  web app
    app_type = "Applications"
    case_list_name = 'Case List'
    form_name = 'Registration Form'
    login_as = 'henry'
    update_case_change_link = "Case Change"
    case_register_form = "Case Register"
    case_update_form = "Update Case"
    case_update_name = "reassign_change"
    daily_form_groups = ["Active Mobile Workers", "Deactivated Mobile Workers"]
    deactivated_user = "deactivate_test_user"

    # Date Filter
    date_having_submissions = "2022-01-18 to 2022-02-18"

    worker_report = "Worker Activity: Requested export excel data"
    email_worker_report = "Worker Activity Report sent via scripts"
    daily_form_report = "Daily Form Activity: Requested export excel data"
    email_daily_form_report = "Daily Form Activity Report sent via scripts"
    case_report = "Case Activity: Requested export excel data"
    email_case_report = "Case Activity Report sent via scripts"
    email_proj_perf_report = "Project Performance Report sent via scripts"
    email_sub_by_form_report = "Submissions By Form Report sent via scripts"
    email_form_comp_report = "Form Completion Time Report sent via scripts"

    reasign_modules_forms = {"Case Change": ["Case Register", "Update Case"],
                             "Case List": ["Android Test Form", "Followup Form", "Registration Form"]}

    default_app_mod_form = ["Show all Forms of this Application Type...", "Show all Forms in selected Application", "Show all Forms in selected Module"]
    default_app_mod_form_fct = ["Select Application...", "Select a Menu", "Select a Form"]
    app_type_list = ["Show all Application Types", "Active CommCare Applications", "Deleted CommCare Applications"]
    fct_app_type_list = ["Select an Application Type", "Active CommCare Applications", "Deleted CommCare Applications"]
    view_form_tabs = ["Form Properties", "Case Changes", "Form Metadata", "Raw XML"]