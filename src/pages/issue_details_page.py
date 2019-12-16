import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException

from src.pages.base_page import BasePage

class IssueDetailsPage(BasePage):

    def is_edit_button_present(self):
        __edit_button = self.browser.find_element(By.CSS_SELECTOR, "#edit-issue .trigger-label")

    def click_issue_reporter_field(self):
        for i in range(3):
            try:
                __reporter_field = WebDriverWait(self.browser, self.wait).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#assignee-val>span[class='user-hover']")))
                return self.browser.find_element(By.CSS_SELECTOR, "#assignee-val>span[class='user-hover']").click()

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                ElementClickInterceptedException):
                    time.sleep(self.sleepTimeForRetry['fast'])
                    i += 1

    def enter_new_reporter(self, name):
            for i in range(3):
                try:
                    self.browser.find_element(By.CSS_SELECTOR, "#assignee-field").send_keys(name)
                    self.browser.find_element(By.CSS_SELECTOR, "#assignee-field").send_keys(Keys.ENTER)
                    self.browser.find_element(By.CSS_SELECTOR, ".aui-iconfont-success").click()

                except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                        time.sleep(self.sleepTimeForRetry['fast'])
                        i += 1

    def should_be_new_assigner(self):
        for i in range(3):
            try:
                __is_new_assigner = self.browser.find_element(By.CSS_SELECTOR, "#assignee-val>span[class='user-hover']")
                return __is_new_assigner.text
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException,
                    ElementNotInteractableException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i +=1

        __is_new_assigner = self.browser.find_element(By.CSS_SELECTOR, "#assignee-val>span[class='user-hover']")
        return __is_new_assigner.text


    def refresh_the_page(self):
        self.browser.refresh()