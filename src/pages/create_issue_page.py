import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage


class CreateIssue(BasePage):

    def should_have_title(self, title):
        for i in range(3):
            try:
                __create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title='Create Issue']").text
                if title in __create_issue_title:
                    break
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException,
                    ElementNotInteractableException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1

    def choose_the_project(self, project_name):
        wait = WebDriverWait(self.browser, self.wait)
        element = wait.until(EC.visibility_of_element_located((By.ID, 'project-field')))
        element.clear()
        element.send_keys(project_name)
        element.send_keys(Keys.TAB)
        self.wait_for_spinner((By.CSS_SELECTOR, ".aui-spinner"))

    def click_create_issue_button_at_details_page(self):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#create-issue-submit")).click()


    def enter_summary_field(self, summary):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#summary")).send_keys(summary)

    def enter_reporter(self, reporter):
        __reporter_field = self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#reporter-field"))
        __reporter_field.click()
        __reporter_field.clear()
        __reporter_field.send_keys(reporter)
        __reporter_field.send_keys(Keys.TAB)


    def is_alert_present(self):
        for i in range(3):
            try:
                __issue = self.browser.find_element_by_css_selector(".aui-will-close")
                if __issue.is_displayed():
                    return __issue.text
            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1
