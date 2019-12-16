import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CommentPage(BasePage):

    def click_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#footer-comment-button").click()

    def enter_comment_text(self, comment_text):

        for i in range(3):
            try:
                input_field = self.browser.find_element(By.CSS_SELECTOR, "#comment")
                if input_field.is_displayed():
                    return input_field.send_keys(comment_text)
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying " + str(i) + " attempts")

    def click_add_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#issue-comment-add-submit").click()

    def comment_input_field_at_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#comment").is_displayed

