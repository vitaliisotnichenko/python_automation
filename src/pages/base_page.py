class BasePage():

    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)

    def open(self, url):
        self.browser.get(url)

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.browser.title