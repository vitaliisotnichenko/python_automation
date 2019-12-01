from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class LoginPage(BasePage):


    def login_to_jira_enter_username(self):
        # type: (WebDriver) -> ()
        self.browser.find_element(By.CSS_SELECTOR, "#login-form-username").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#login-form-username").send_keys("webinar5")

    def login_to_jira_enter_password(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login-form-password").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#login-form-password").send_keys("webinar5")

    def click_login_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login").click()

    def should_contain_assigned_to_me_section(self):
        profile = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#gadget-10002-title"))).text
        assert "Assigned to Me" in profile




