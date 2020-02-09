
from selenium.webdriver.common.by import By

from .base_page import BasePage

class MainPage(BasePage):

    def is_create_issue_button(self):
        __create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title='Create Issue']").text
        return "Create Issue" in __create_issue_title

    def click_create_issue_button(self):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#create_link")).click()

    def is_assigned_to_me_section(self):
        __element = self.wait_element_to_be_located((By.CSS_SELECTOR, "#gadget-10002-title")).text
        return "Assigned to Me" in __element

    def click_the_first_ticket_assigned_to_me(self):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, ".hide-carrot tr:nth-child(1)[class='issuerow']>td+[class=issuekey]>a")).click()

