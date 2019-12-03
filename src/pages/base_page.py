class BasePage():

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.browser.title