import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class TicketDetails(BasePage):

    def click_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#footer-comment-button").click()

    def enter_comment_text(self):
        # time.sleep(5)
        for i in range(3):
            try:
                input_field = self.browser.find_element(By.CSS_SELECTOR, ".mce-content-body")
                if input_field.is_displayed():
                    return input_field.send_keys("comment_text")
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying " + str(i) + " attempts")
        # self.browser.find_element(By.CSS_SELECTOR, ".mce-content-body").send_keys("comment_text")
        # WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(By.CSS_SELECTOR, ".mce-content-body")).send_keys("comment_text")
        # __enter_text.send_keys(comment_text)

    def click_add_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#issue-comment-add-submit").click()