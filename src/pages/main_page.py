import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class MainPage(BasePage):

    def is_create_issue_button(self):
        __create_issue_title = self.browser.find_element_by_css_selector("[title=\"Create Issue\"]").text
        return "Create Issue" in __create_issue_title

    def is_assigned_to_me_section(self):
        __assigned_to_me_section = WebDriverWait(self.browser, self.wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#gadget-10002-title"))).text
        return "Assigned to Me" in __assigned_to_me_section

    def click_the_first_ticket_assigned_to_me(self):
        for i in range(3):
            try:
                __the_first_issue = self.browser.find_element_by_css_selector(".hide-carrot tr:nth-child(1)[class='issuerow']>td+[class=issuekey]")
                if __the_first_issue.is_displayed():
                    return __the_first_issue.click()

            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                time.sleep(5)
                i += 1
