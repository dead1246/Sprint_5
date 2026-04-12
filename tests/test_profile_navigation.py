from helpers import (
    login_user,
    open_login_page,
    open_main_page,
    open_personal_account,
    register_user,
    wait_for_clickable,
    wait_for_url,
    wait_for_visibility,
)
from locators import AccountPageLocators, LoginPageLocators, MainPageLocators


def test_personal_account_navigation(driver, user_data):
    register_user(driver, user_data)
    open_main_page(driver)
    wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING)
    login_user(driver, user_data["email"], user_data["password"])
    open_personal_account(driver)


def test_transition_from_personal_account_to_constructor_by_constructor_link(
    driver, user_data
):
    register_user(driver, user_data)
    open_login_page(driver)
    login_user(driver, user_data["email"], user_data["password"])
    open_personal_account(driver)
    wait_for_clickable(driver, MainPageLocators.CONSTRUCTOR_LINK).click()

    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)
    wait_for_url(driver, "/")


def test_transition_from_personal_account_to_constructor_by_logo(driver, user_data):
    register_user(driver, user_data)
    open_login_page(driver)
    login_user(driver, user_data["email"], user_data["password"])
    open_personal_account(driver)
    wait_for_clickable(driver, MainPageLocators.STELLAR_BURGERS_LOGO).click()

    wait_for_visibility(driver, MainPageLocators.MAIN_HEADING)
    wait_for_url(driver, "/")


def test_logout_from_personal_account(driver, user_data):
    register_user(driver, user_data)
    open_login_page(driver)
    login_user(driver, user_data["email"], user_data["password"])
    open_personal_account(driver)
    wait_for_clickable(driver, AccountPageLocators.LOGOUT_BUTTON).click()

    wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING)
    wait_for_url(driver, "/login")

