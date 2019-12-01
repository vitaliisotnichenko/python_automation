from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class CreateIssue(BasePage):

    def should_have_title(self):
        create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title=\"Create Issue\"]").text
        assert "Create Issue" in create_issue_title

    def choose_the_project(self):
        select = Select.find_element(By.CSS_SELECTOR, "#project")
        select.select_by_visible_text("Webinar (WEBINAR")

    def click_create_issue_button(self):
        for i in range(3):
            try:
                self.browser.find_element(By.CSS_SELECTOR, "#create_link").click()
                if self.browser.find_element(By.CSS_SELECTOR, "[title='Create Issue']").is_displayed():
                    break
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + " attempt")

    def enter_summary_field(self):
        self.browser.find_element(By.CSS_SELECTOR, "#summary").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#summary").send_keys("UI bug In Jira")


    def enter_reporter(self):
        # type: (WebDriver) -> ()
        self.browser.find_element(By.CSS_SELECTOR, "#reporter-field").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#reporter-field").send_keys("webinar5")
        self.browser.find_element(By.CSS_SELECTOR, "#reporter-field").send_keys(Keys.ENTER)

    def click_create_issue_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#create-issue-submit").click()

    def should_have_text_create_issue_alert(self):
        issue = self.browser.find_element_by_css_selector(".aui-will-close").text
        assert "has been successfully created." in issue