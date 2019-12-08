from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):


    def login_to_jira_enter_username(self, username):
        # type: (WebDriver) -> ()
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






