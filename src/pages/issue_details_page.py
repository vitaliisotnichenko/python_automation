import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException

from src.pages.base_page import BasePage

class IssueDetailsPage(BasePage):

    def is_edit_button_present(self):
        __edit_button = self.browser.find_element(By.CSS_SELECTOR, "#edit-issue .trigger-label")

    def click_issue_reporter_field(self):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#assignee-val>span[class='user-hover']")).click()

    def enter_new_reporter(self, name):
        for i in range(2):
            try:
                 if self.browser.find_element(By.CSS_SELECTOR, "#assignee-field").send_keys(name):
                     return True

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                    time.sleep(self.sleepTimeForRetry['medium'])
                    i+=1

        self.browser.find_element(By.CSS_SELECTOR, "#assignee-field").send_keys(Keys.TAB)
        self.browser.find_element(By.CSS_SELECTOR, ".aui-iconfont-success").click()

    def should_be_new_assigner(self, __expected_assigner):
        for i in range(3):
            try:
                __is_new_assigner = self.browser.find_element(By.CSS_SELECTOR, "#assignee-val>span[class='user-hover']")
                __name_of_assigner = __is_new_assigner.text
                return __expected_assigner == __name_of_assigner
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException,
                    ElementNotInteractableException):
                time.sleep(self.sleepTimeForRetry['medium'])
                i +=1


    def refresh_the_page(self):
        self.browser.refresh()