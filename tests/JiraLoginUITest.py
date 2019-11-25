import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class TestJiraLoginUI:

    def test_login_to_jira(self):
        driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        assert "System Dashboard - Hillel IT School JIRA" in driver.title
        driver.find_element_by_css_selector("#login-form-username").send_keys("webinar5")
        driver.find_element_by_css_selector("#login-form-password").send_keys("webinar5")
        driver.find_element_by_css_selector("#login").click()
        time.sleep(3)
        profile = driver.find_element_by_css_selector("#gadget-10002-title").text
        assert "Assigned to Me" in profile
        driver.quit()


    def test_create_issue_in_jira(self):
        driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        assert "System Dashboard - Hillel IT School JIRA" in driver.title
        driver.find_element_by_css_selector("#login-form-username").send_keys("webinar5")
        driver.find_element_by_css_selector("#login-form-password").send_keys("webinar5")
        driver.find_element_by_css_selector("#login").click()
        time.sleep(5)
        driver.find_element_by_css_selector("#create_link").click()
        create_issue_title = driver.find_element_by_css_selector("[title=\"Create Issue\"]").text
        assert "Create Issue" in create_issue_title
        driver.find_element_by_css_selector("#summary").clear()
        driver.find_element_by_css_selector("#summary").send_keys("UI bug In Jira")
        driver.find_element_by_css_selector("#reporter-field").clear()
        driver.find_element_by_css_selector("#reporter-field").send_keys("webinar5")
        driver.find_element_by_css_selector("#reporter-field").click()
        driver.find_element_by_css_selector("#create-issue-submit").click()
        issue = driver.find_element_by_css_selector(".aui-will-close").text
        assert "has been successfully created." in issue
        driver.quit()

        # TODO