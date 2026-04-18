import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data.credentials import build_user
from helpers import register_user


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Браузер для запуска UI-тестов",
    )


def build_browser(browser_name: str):
    if browser_name == "firefox":
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)

    browser.maximize_window()
    return browser


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    browser = build_browser(browser_name)
    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    return build_user()


@pytest.fixture(scope="session")
def registered_user(request):
    user = build_user()
    browser_name = request.config.getoption("--browser")
    browser = build_browser(browser_name)

    try:
        register_user(browser, user)
    finally:
        browser.quit()

    return user
