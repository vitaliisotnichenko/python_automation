import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.login_page import LoginPage
from src.pages.create_issue_page import CreateIssue
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class TestJiraLoginUI:

    def test_login_to_jira(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.should_have_title_at_page()
        login_page.login_to_jira_enter_username()
        login_page.login_to_jira_enter_password()
        login_page.click_login_button()
        login_page.should_contain_assigned_to_me_section()



    # def test_create_issue_in_jira(self, browser):
    #     login_page = LoginPage(browser)
    #     login_page.open()
    #     browser.set_network_conditions(
    #
    #         offline=False,
    #         latency=1,  # additional latency (ms)
    #         download_throughput=250 * 1024,  # maximal throughput
    #         upload_throughput=250 * 1024)  # maximal throughput
    #
    #     login_page.should_have_title_at_page()
    #     login_page.login_to_jira_enter_username()
    #     login_page.login_to_jira_enter_password()
    #     login_page.click_login_button()
    #     login_page.should_contain_assigned_to_me_section()
    #     create_issue_page = CreateIssue(browser)
    #     time.sleep(5)
    #     browser.find_element_by_css_selector("#create_link").click()
    #     for i in range(3):
    #         try:
        #         browser.find_element_by_css_selector("#create_link").click()
        #         if browser.find_element_by_css_selector("[title='Create Issue']").is_displayed():
        #             break
        #     except (NoSuchElementException, StaleElementReferenceException):
        #         time.sleep(5)
        #         i += 1
        #         print("Couldn't find element. Retrying... " + str(i) + "attempt")

