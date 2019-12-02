from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def click_login_button(self):
        __login_button = self.browser.find_element(By.CSS_SELECTOR, "#login").click()

    # def is_assigned_to_me_section(self):
    #     __assigned_to_me_section = WebDriverWait(self.browser, 30).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#gadget-10002-title"))).text
    #     assert "Assigned to Me" in __assigned_to_me_section





