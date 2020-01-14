import pytest
from global_scope import global_user, global_pass, url_ui
from src.pages.login_page import LoginPage
from src.pages.create_issue_page import CreateIssue
from src.pages.main_page import MainPage
from src.pages.comment_page import CommentPage
from src.pages.issue_details_page import IssueDetailsPage

class TestJiraLoginUI:

    @pytest.mark.smoke
    def test_login_to_jira(self, browser):
        self.login_page = LoginPage(browser)
        self.login_page.open(url_ui)
        assert self.login_page.at_page()
        self.login_page.login_to_jira_enter_username(global_user)
        self.login_page.login_to_jira_enter_password(global_pass)
        self.login_page.click_login_button_at_main_page()
        self.main_page = MainPage(browser)
        self.main_page.is_assigned_to_me_section()
        assert self.main_page.is_assigned_to_me_section()

    @pytest.mark.smoke
    def test_create_issue_in_jira(self, browser):
        self.login_page = LoginPage(browser)
        self.login_page.open("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        assert self.login_page.at_page()
        self.login_page.login_to_jira_enter_username("webinar5")
        self.login_page.login_to_jira_enter_password("webinar5")
        self.login_page.click_login_button_at_main_page()
        self.main_page = MainPage(browser)
        assert self.main_page.is_assigned_to_me_section()
        self.main_page.click_create_issue_button()
        self.create_issue_page = CreateIssue(browser)
        self.create_issue_page.should_have_title()
        self.create_issue_page.choose_the_project("Webinar (WEBINAR)")
        self.create_issue_page.enter_summary_field("UI bug In Jira")
        self.create_issue_page.enter_reporter("webinar5")
        self.create_issue_page.click_create_issue_button_at_details_page()
        assert self.create_issue_page.is_alert_present()


    @pytest.mark.regression
    def test_add_comment_to_the_ticket(self, browser):
        self.login_page = LoginPage(browser)
        self.login_page.open("https://jira.hillel.it/browse/WEBINAR-9060")
        self.login_page.login_to_jira_enter_username("webinar5")
        self.login_page.login_to_jira_enter_password("webinar5")
        self.login_page.click_login_button_at_login_page()
        self.comment_page_page = CommentPage(browser)
        self.comment_page_page.click_comment_button()
        self.comment_page_page.enter_comment_text("comment_text")
        self.comment_page_page.click_add_comment_button()
        assert not self.comment_page_page.comment_input_field_at_page(), "Comment not added"


    @pytest.mark.regression
    def test_change_assigner_for_the_ticket(self, browser):
        self.login_page = LoginPage(browser)
        self.login_page.open("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        self.login_page.login_to_jira_enter_username("webinar5")
        self.login_page.login_to_jira_enter_password("webinar5")
        self.login_page.click_login_button_at_main_page()
        self.main_page = MainPage(browser)
        self.main_page.click_the_first_ticket_assigned_to_me()
        self.issue_details_page = IssueDetailsPage(browser)
        self.issue_details_page.click_issue_reporter_field()
        self.issue_details_page.enter_new_reporter("Artur Piluck")
        assert self.issue_details_page.should_be_new_assigner("Artur Piluck")
        self.issue_details_page.refresh_the_page()
        assert self.issue_details_page.should_be_new_assigner("Artur Piluck")


    @pytest.mark.regression
    @pytest.mark.parametrize("login, password, rez",
    [
        ("admin", "password", "Sorry, your username and password are incorrect - please try again.")

    ])
    def test_with_invalid_login_to_jira(self, browser, login, password, rez):
        self.login_page = LoginPage(browser)
        self.login_page.open(url_ui)
        assert self.login_page.at_page()
        self.login_page.login_to_jira_enter_username(login)
        self.login_page.login_to_jira_enter_password(password)
        self.login_page.click_login_button_at_main_page()
        assert self.login_page.is_invalid_message_present(rez)







