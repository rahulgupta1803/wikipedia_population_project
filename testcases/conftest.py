import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        print("launching Chrome")
        driver= webdriver.Chrome()
    elif browser=='firefox':
        print("launching Firefox")
        driver=webdriver.Firefox()
    elif browser=='edge':
        print("launching Edge")
        driver=webdriver.Edge()
    else:
        print("launching headless")
        options=webdriver.ChromeOptions()
        options.add_argument('headless')
        driver=webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get("https://en.wikipedia.org/wiki/Demographics_of_India")
    yield driver
    driver.quit()
    return driver
