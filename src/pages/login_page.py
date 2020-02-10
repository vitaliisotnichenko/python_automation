import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):


    def login_to_jira_enter_username(self, username):
        __username_field = self.browser.find_element(By.CSS_SELECTOR, "#login-form-username")
        __username_field.clear()
        __username_field.send_keys(username)

    def login_to_jira_enter_password(self, password):
        __password_field = self.browser.find_element(By.CSS_SELECTOR, "#login-form-password")
        __password_field.clear()
        __password_field.send_keys(password)

    def click_login_button_at_main_page(self):
        __login_button = self.browser.find_element(By.CSS_SELECTOR, "#login").click()

    def click_login_button_at_login_page(self):
        __login_button = self.browser.find_element(By.CSS_SELECTOR, "#login-form-submit").click()

    def is_invalid_message_present(self, error_message):
        for i in range(3):
            try:
                if self.browser.find_element(By.CSS_SELECTOR, "#usernameerror>p").is_displayed():
                    return error_message == self.browser.find_element(By.CSS_SELECTOR, "#usernameerror>p").text
            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1



