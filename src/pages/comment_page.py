from selenium.webdriver.common.by import By
from .base_page import BasePage

class CommentPage(BasePage):

    def click_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#footer-comment-button").click()

    def enter_comment_text(self, comment_text):
        self.wait_element_to_be_present((By.CSS_SELECTOR, "#comment")).send_keys(comment_text)

    def click_add_comment_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#issue-comment-add-submit").click()

    def comment_is_present(self, comment_text):
        return self.browser.find_element(By.XPATH, "//*[@id='issue_actions_container']//child::*[contains(text(),'comment_text')]").is_displayed

