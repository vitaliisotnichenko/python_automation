import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    sleepTimeForRetry = {'slow': 20, 'medium': 15, 'fast': 5, 'very fast': 3}

    def __init__(self, browser, wait=10):
        self.browser = browser
        self.wait = wait

    def open(self, url):
        self.browser.get(url)
        self.browser.maximize_window()

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.browser.title

    def wait_element_to_be_clickable(self, locator) -> WebElement:
        for i in range(3):
            try:
                __wait_element_to_be_clickable = WebDriverWait(self.browser, self.wait).until(
                    EC.element_to_be_clickable(locator))
                if __wait_element_to_be_clickable.is_displayed():
                    return __wait_element_to_be_clickable

            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException,
                    ElementNotInteractableException):
                time.sleep(self.sleepTimeForRetry['medium'])
                i += 1
                print("Couldn't find element. Retrying " + str(i) + " attempts")


    def wait_for_spinner(self, locator):
        for i in range(2):
            try:
                __spinner = WebDriverWait(self.browser, 20).until(
                    EC.visibility_of_element_located(locator))
                time.sleep(self.sleepTimeForRetry['fast'])
                return True

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
                    ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1

