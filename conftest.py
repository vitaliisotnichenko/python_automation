import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()


email = ["admin"]
password = ["password"]
result =["Sorry, your username and password are incorrect - please try again."]

@pytest.fixture(params=email)
def parameters_email(request):
    return request.param

@pytest.fixture(params=password)
def parameters_password(request):
    return request.param

@pytest.fixture(params=result)
def parameters_result(request):
    return request.param