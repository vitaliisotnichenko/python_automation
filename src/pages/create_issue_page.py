from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
import time
from .base_page import BasePage

class CreateIssue(BasePage):

    def should_have_create_issue_title(self):
        create_issue_title = self.browser.find_element_by_css_selector("[title=\"Create Issue\"]").text
        assert "Create Issue" in create_issue_title

    def choose_the_project(self):
        select = Select(self.browser.find_element_by_css_selector("#project"))
        select.select_by_visible_text("Webinar (WEBINAR)")

    def wait_create_issue_button(self):
        for i in range(3):
            try:
                self.browser.find_element_by_css_selector("#create_link").click()
                if self.browser.find_element_by_css_selector("[title='Create Issue']").is_displayed():
                    break
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + "attempt")