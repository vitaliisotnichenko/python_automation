from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
import time


class CreateIssue(BasePage):

    def should_have_title(self):
        for i in range(3):
            try:
                __create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title='Create Issue']").text
                if "Create Issue" in __create_issue_title:
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
        self.wait_for_spinner()

    def click_create_issue_button_at_details_page(self):
        self.wait_element_to_be_present((By.CSS_SELECTOR, "#create-issue-submit")).click()


    def enter_summary_field(self, summary):
        for i in range(3):
            try:
                __enter_summary_field = WebDriverWait(self.browser, self.wait).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#summary")))

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['medium'])
                i += 1
        __enter_summary_field.send_keys(summary)

    def wait_for_spinner(self):
        for i in range(2):
            try:
                __spinner = WebDriverWait(self.browser, 20).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".aui-spinner")))
                time.sleep(self.sleepTimeForRetry['fast'])
                return True

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1

    def enter_reporter(self, reporter):
        for i in range(3):
            try:
                __reporter_field = WebDriverWait(self.browser, self.wait).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#reporter-field")))
                __reporter_field.clear()
                __reporter_field.send_keys(reporter)
                __reporter_field.send_keys(Keys.TAB)

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['medium'])
                i += 1

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
