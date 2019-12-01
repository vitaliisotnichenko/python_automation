class BasePage:

    def __init__(self, browser):
        self.browser = browser
        # self.url = url

    def open(self):
        # self.browser.get(self.url)
        self.browser.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")

    def should_have_title_at_page(self):
        assert "System Dashboard - Hillel IT School JIRA" in self.browser.title