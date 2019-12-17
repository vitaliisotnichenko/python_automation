class BasePage():

    sleepTimeForRetry = {'slow':20, 'very fast': 10, 'fast': 5, 'medium': 10}

    def __init__(self, browser, wait = 10):
        self.browser = browser
        self.wait = wait

    def open(self, url):
        self.browser.get(url)
        self.browser.maximize_window()

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.browser.title

