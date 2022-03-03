from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jsm.pages.agent_pages import Login
from util.conf import JSM_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action

    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         if login_page.is_first_login():
    #             login_page.first_login_setup()
    #         if login_page.is_first_login_second_page():
    #             login_page.first_login_second_page_setup()
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_agent_app_custom_action")
    def app_specific_action_log_level_web_action(webdriver, datasets):
        page = BasePage(webdriver)

        @print_timing("selenium_agent_app_custom_action_log_level_web_action")
        def measure():
            @print_timing("selenium_agent_app_custom_action:log_level_web_action")
            def sub_measure():
                page.go_to_url(
                    f"{JSM_SETTINGS.server_url}/secure/LogLevel.jspa")
                page.wait_until_visible((By.ID, "log-level-main-panel"))

            sub_measure()

        measure()
