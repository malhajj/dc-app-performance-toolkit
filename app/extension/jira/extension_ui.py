from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS


def app_specific_action_notification_settings(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_notification_settings")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NotifierConfigWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "prefrences-page-link"))
    measure()


def app_specific_action_notification_scheme(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_notification_scheme")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NotifierConfigWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "nfj-admin-page"))
    measure()


def app_specific_action_notifications_menu(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_notification_scheme")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NfjSchemesWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "nfj-schemes-page"))
    measure()

