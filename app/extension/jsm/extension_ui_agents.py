from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jsm.pages.agent_pages import Login
from util.conf import JSM_SETTINGS


def app_specific_action_log_level_web_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_log_level_web_action")
    def measure():
        @print_timing("selenium_agent_app_custom_action:log_level_web_action")
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/secure/LogLevel.jspa")
            page.wait_until_visible((By.ID, "log-level-panel"))

        sub_measure()

    measure()