from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class CreateIssue(BasePage):

    def should_have_title(self):
        __create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title=\"Create Issue\"]").text
        return "Create Issue" in __create_issue_title

    def choose_the_project(self):
        __select = Select.find_element(By.CSS_SELECTOR, "#project")
        __select.select_by_visible_text("Webinar (WEBINAR")

    def click_create_issue_button(self):
        for i in range(3):
            try:
                __create_issue_button = self.browser.find_element(By.CSS_SELECTOR, "#create_link")
                __create_issue_button.click()
                if __create_issue_button.is_displayed():
                    break
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + " attempt")

    def enter_summary_field(self):
        __summary_field = self.browser.find_element(By.CSS_SELECTOR, "#summary")
        __summary_field.clear()
        __summary_field.send_keys("UI bug In Jira")


    def enter_reporter(self):
        # type: (WebDriver) -> ()
        __reporter_field = self.browser.find_element(By.CSS_SELECTOR, "#reporter-field")
        __reporter_field.clear()
        __reporter_field.send_keys("webinar5")
        __reporter_field.send_keys(Keys.ENTER)

    # def click_create_issue_button(self):
    #     __create_issue_button = self.browser.find_element(By.CSS_SELECTOR, "#create-issue-submit").click()

    def is_alert_present(self):
        __issue = self.browser.find_element_by_css_selector(".aui-will-close").text
        return "Create Issue" in __issue