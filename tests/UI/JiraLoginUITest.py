import time
from src.pages.login_page import LoginPage
from src.pages.create_issue_page import CreateIssue
from src.pages.main_page import MainPage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestJiraLoginUI:

    def test_login_to_jira(self, browser):
        # type: (WebDriver) -> ()
        self.login_page = LoginPage(browser)
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login_to_jira_enter_username("webinar5")
        self.login_page.login_to_jira_enter_password("webinar5")
        self.login_page.click_login_button()
        self.main_page = MainPage(browser)
        self.main_page.is_assigned_to_me_section()
        assert self.main_page.is_assigned_to_me_section()


    def test_create_issue_in_jira(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.should_have_title_at_page()
        login_page.login_to_jira_enter_username()
        login_page.login_to_jira_enter_password()
        login_page.click_login_button()
        login_page.should_contain_assigned_to_me_section()
        main_page = MainPage(browser)
        main_page.should_have_create_issue_button()
        create_issue_page = CreateIssue(browser)
        create_issue_page.click_create_issue_button()
        create_issue_page.should_have_title()
        create_issue_page.choose_the_project()
        create_issue_page.enter_summary_field()
        create_issue_page.enter_reporter()
        create_issue_page.click_create_issue_button()
        issue = create_issue_page.is_alert_present()
        assert "has been successfully created." in issue

