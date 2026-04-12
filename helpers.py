from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import (
    AccountPageLocators,
    ConstructorPageLocators,
    LoginPageLocators,
    MainPageLocators,
    RegisterPageLocators,
)


BASE_URL = "https://stellarburgers.education-services.ru"
WAIT_TIMEOUT = 10


def wait_for_visibility(driver: WebDriver, locator: tuple[str, str]):
    return WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver: WebDriver, locator: tuple[str, str]):
    return WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_url(driver: WebDriver, url_part: str):
    WebDriverWait(driver, WAIT_TIMEOUT).until(EC.url_contains(url_part))


def click_with_js(driver: WebDriver, locator: tuple[str, str]):
    element = wait_for_visibility(driver, locator)
    driver.execute_script("arguments[0].click();", element)


def open_main_page(driver: WebDriver):
    driver.get(BASE_URL)
    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)


def open_login_page(driver: WebDriver):
    driver.get(f"{BASE_URL}/login")
    wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING)


def open_register_page(driver: WebDriver):
    driver.get(f"{BASE_URL}/register")
    wait_for_visibility(driver, RegisterPageLocators.REGISTER_HEADING)


def fill_registration_form(driver: WebDriver, user: dict[str, str]):
    wait_for_visibility(driver, RegisterPageLocators.NAME_INPUT).send_keys(user["name"])
    wait_for_visibility(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(user["email"])
    wait_for_visibility(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(
        user["password"]
    )


def submit_registration(driver: WebDriver):
    wait_for_clickable(driver, RegisterPageLocators.REGISTER_BUTTON).click()


def register_user(driver: WebDriver, user: dict[str, str]):
    open_register_page(driver)
    fill_registration_form(driver, user)
    submit_registration(driver)
    wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING)
    wait_for_url(driver, "/login")


def login_user(driver: WebDriver, email: str, password: str):
    wait_for_visibility(driver, LoginPageLocators.EMAIL_INPUT).send_keys(email)
    wait_for_visibility(driver, LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    wait_for_clickable(driver, LoginPageLocators.LOGIN_BUTTON).click()
    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)


def open_personal_account(driver: WebDriver):
    wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    wait_for_visibility(driver, AccountPageLocators.LOGOUT_BUTTON)
    wait_for_url(driver, "/account")


def switch_to_sauces(driver: WebDriver):
    sauce_section = wait_for_visibility(driver, ConstructorPageLocators.SAUCES_SECTION)
    driver.execute_script("arguments[0].scrollIntoView();", sauce_section)
    click_with_js(driver, ConstructorPageLocators.SAUCES_TAB)
    wait_for_visibility(driver, ConstructorPageLocators.ACTIVE_SAUCES_TAB)


def switch_to_fillings(driver: WebDriver):
    filling_section = wait_for_visibility(
        driver, ConstructorPageLocators.FILLINGS_SECTION
    )
    driver.execute_script("arguments[0].scrollIntoView();", filling_section)
    click_with_js(driver, ConstructorPageLocators.FILLINGS_TAB)
    wait_for_visibility(driver, ConstructorPageLocators.ACTIVE_FILLINGS_TAB)


def switch_to_buns(driver: WebDriver):
    buns_section = wait_for_visibility(driver, ConstructorPageLocators.BUNS_SECTION)
    driver.execute_script("arguments[0].scrollIntoView();", buns_section)
    click_with_js(driver, ConstructorPageLocators.BUNS_TAB)
    wait_for_visibility(driver, ConstructorPageLocators.ACTIVE_BUNS_TAB)
