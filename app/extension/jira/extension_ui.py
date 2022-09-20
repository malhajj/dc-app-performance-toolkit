from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS


def app_specific_action_notification_settings(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_notification_settings")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NotifierConfigWebActionSupport.jspa")
        page.wait_until_visible((By.ID, "fcm-notifier-status-on"))
    measure()


def app_specific_action_notification_scheme(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_notification_scheme")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/NotificationSchemaWebAction.jspa?projectKey=KAN")
        page.wait_until_visible((By.ID, "nfj-default-notification-schema"))
    measure()


def app_specific_action_notifications_menu(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_notification_scheme")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/upm?source=side_nav_manage_addons")
        page.wait_until_visible((By.ID, "nfj-notifications-dropdown-menu"))
    measure()

