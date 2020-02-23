import pytest
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    grid_url = "http://localhost:4444/wd/hub"
    desired_caps = DesiredCapabilities.CHROME
    browser = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
    yield browser
    browser.quit()
# @pytest.fixture(scope="function")
# def browser():
#     browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     yield browser
#     browser.quit()

