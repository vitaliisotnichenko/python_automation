class BasePage():

    def __init__(self, browser, wait = 10):
        self.browser = browser
        self.wait = wait

    def open(self, url):
        self.browser.get(url)
        self.browser.maximize_window()

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.browser.title

