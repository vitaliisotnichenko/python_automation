
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage


class CreateIssue(BasePage):

    def should_have_title(self):
        self.wait_text_of_element_to_be_present((By.CSS_SELECTOR, "[title='Create Issue']", "Create Issue"))

    def choose_the_project(self, project_name):
        wait = WebDriverWait(self.browser, self.wait)
        element = wait.until(EC.visibility_of_element_located((By.ID, 'project-field')))
        element.clear()
        element.send_keys(project_name)
        element.send_keys(Keys.TAB)
        self.wait_for_spinner()

    def click_create_issue_button_at_details_page(self):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#create-issue-submit")).click()


    def enter_summary_field(self, summary):
        self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#summary")).send_keys(summary)

    def wait_for_spinner_at_page(self):
        self.wait_for_spinner((By.CSS_SELECTOR, ".aui-spinner"))

    def enter_reporter(self, reporter):
        __reporter_field = self.wait_element_to_be_clickable((By.CSS_SELECTOR, "#reporter-field"))
        __reporter_field.click()
        __reporter_field.clear()
        __reporter_field.send_keys(reporter)
        __reporter_field.send_keys(Keys.TAB)

    def is_alert_present(self):
        self.text_of_element_to_be_present((By.CSS_SELECTOR, ".aui-will-close"))

