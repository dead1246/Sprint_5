from helpers import (
    login_user,
    open_login_page,
    open_main_page,
    open_register_page,
    register_user,
    wait_for_clickable,
    wait_for_visibility,
)
from locators import (
    ForgotPasswordPageLocators,
    LoginPageLocators,
    MainPageLocators,
    RegisterPageLocators,
)


def test_login_from_main_page_button(driver, user_data):
    register_user(driver, user_data)
    open_main_page(driver)
    wait_for_clickable(driver, MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

    login_user(driver, user_data["email"], user_data["password"])
    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)


def test_login_from_personal_account_button(driver, user_data):
    register_user(driver, user_data)
    open_main_page(driver)
    wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    login_user(driver, user_data["email"], user_data["password"])
    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)


def test_login_from_registration_form(driver, user_data):
    register_user(driver, user_data)
    open_register_page(driver)
    wait_for_clickable(driver, RegisterPageLocators.LOGIN_LINK).click()

    login_user(driver, user_data["email"], user_data["password"])
    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)


def test_login_from_forgot_password_form(driver, user_data):
    register_user(driver, user_data)
    open_login_page(driver)
    wait_for_clickable(driver, LoginPageLocators.FORGOT_PASSWORD_LINK).click()
    wait_for_visibility(driver, ForgotPasswordPageLocators.FORGOT_PASSWORD_HEADING)
    wait_for_clickable(driver, ForgotPasswordPageLocators.LOGIN_LINK).click()

    login_user(driver, user_data["email"], user_data["password"])
    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)
