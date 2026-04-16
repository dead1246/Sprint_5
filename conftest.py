import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data.credentials import build_user


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Браузер для запуска UI-тестов",
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "firefox":
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    return build_user()

