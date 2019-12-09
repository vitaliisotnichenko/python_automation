from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class MainPage(BasePage):

    def is_create_issue_button(self):
        __create_issue_title = self.browser.find_element_by_css_selector("[title=\"Create Issue\"]").text
        return "Create Issue" in __create_issue_title

    def is_assigned_to_me_section(self):
        __assigned_to_me_section = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#gadget-10002-title"))).text
        return "Assigned to Me" in __assigned_to_me_section