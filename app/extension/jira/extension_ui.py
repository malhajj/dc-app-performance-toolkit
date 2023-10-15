from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS
from selenium_ui.jira.pages.pages import Login

# def app_specific_action_notification_settings(webdriver, datasets):
#     page = BasePage(webdriver)

#     @print_timing("selenium_app_specific_user_login")
#     def measure():
#         def app_specific_user_login(username='admin', password='admin'):
#             login_page = Login(webdriver)
#             login_page.delete_all_cookies()
#             login_page.go_to()
#             login_page.set_credentials(username=username, password=password)
#             if login_page.is_first_login():
#                 login_page.first_login_setup()
#             if login_page.is_first_login_second_page():
#                 login_page.first_login_second_page_setup()
#             login_page.wait_for_page_loaded()
#         app_specific_user_login(username='admin', password='admin')
#     measure()

#     @print_timing("selenium_app_custom_action_notification_settings")
#     def measure():
#         page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NotifierConfigWebActionSupport.jspa")
#         page.wait_until_visible((By.ID, "prefrences-page-link"))
#     measure()


def app_specific_action_notification_scheme(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
    measure()

    @print_timing("selenium_app_custom_action_notification_scheme")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NotifierConfigWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "nfj-admin-page"))
    measure()


def app_specific_action_notifications_menu(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
    measure()

    @print_timing("selenium_app_custom_action_notification_scheme")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NfjSchemesWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "nfj-schemes-page"))
    measure()

