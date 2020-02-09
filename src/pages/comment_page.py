import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CommentPage(BasePage):

    def click_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#footer-comment-button").click()

    def enter_comment_text(self, comment_text):
        __element = self.element_to_be_present((By.CSS_SELECTOR, "#comment"))
        __element.send_keys(comment_text)

    def click_add_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#issue-comment-add-submit").click()

    def comment_input_field_at_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#comment").is_displayed

