import random

from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS
from selenium_ui.jira.pages.pages import Login

def app_specific_action_mfj_branded_test1(webdriver, datasets):
    page = BasePage(webdriver)

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
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

    @print_timing("app_specific_action_mfj_branded_test1")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/BrandedMobileSettingsWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "notificationStatusOn"))
    measure()

def app_specific_action_mfj_branded_test2(webdriver, datasets):
    page = BasePage(webdriver)

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
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

    @print_timing("app_specific_action_mfj_branded_test2")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/mfjb/generalConfig")
        page.wait_until_visible((By.ID, "s2id_intervalMaxValue"))
    measure()

def app_specific_action_mfj_branded_test3(webdriver, datasets):
    page = BasePage(webdriver)

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
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

    @print_timing("app_specific_action_mfj_branded_test3")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/BrandedMobileUsageReportAction.jspa")
        page.wait_until_visible((By.ID, "mfjb-usage-report-container"))
    measure()