from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class LoginPage(BasePage):


    def login_to_jira_enter_username(self):
        # type: (WebDriver) -> ()
        __username_field = self.browser.find_element(By.CSS_SELECTOR, "#login-form-username")
        __username_field.clear()
        __username_field.send_keys("webinar5")

    def login_to_jira_enter_password(self):
        __password_field = self.browser.find_element(By.CSS_SELECTOR, "#login-form-password")
        __password_field.clear()
        __password_field.send_keys("webinar5")

    def click_login_button(self):
        __login_button = self.browser.find_element(By.CSS_SELECTOR, "#login").click()

    def should_contain_assigned_to_me_section(self):
        __profile = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#gadget-10002-title"))).text
        assert "Assigned to Me" in __profile

    def should_have_create_issue_button(self):
        __create_issue_title = self.browser.find_element_by_css_selector("[title=\"Create Issue\"]").text
        assert "Create Issue" in __create_issue_title



