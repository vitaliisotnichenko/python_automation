import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.login_page import LoginPage
from src.pages.create_issue_page import CreateIssue
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class TestJiraLoginUI:

    # def test_login_to_jira(self, browser):
    #     login_page = LoginPage(browser)
    #     login_page.open()
    #     login_page.should_have_title_at_page()
    #     login_page.login_to_jira_enter_username()
    #     login_page.login_to_jira_enter_password()
    #     login_page.click_login_button()
    #     login_page.should_contain_assigned_to_me_section()

    def test_create_issue_in_jira(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.should_have_title_at_page()
        login_page.login_to_jira_enter_username()
        login_page.login_to_jira_enter_password()
        login_page.click_login_button()
        login_page.should_contain_assigned_to_me_section()
        login_page.should_have_create_issue_title()
        create_issue_page = CreateIssue(browser)
        create_issue_page.click_create_issue_button()
        create_issue_page.should_have_title()
        create_issue_page.choose_the_project()
        create_issue_page.enter_summary_field()
        create_issue_page.enter_reporter()
        create_issue_page.click_create_issue_button()
        create_issue_page.should_have_text_create_issue_alert()

