import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()
