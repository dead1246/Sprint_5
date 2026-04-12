from helpers import (
    fill_registration_form,
    open_register_page,
    submit_registration,
    wait_for_url,
    wait_for_visibility,
)
from locators import LoginPageLocators, RegisterPageLocators


def test_successful_registration(driver, user_data):
    open_register_page(driver)
    fill_registration_form(driver, user_data)
    submit_registration(driver)

    wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING)
    wait_for_url(driver, "/login")


def test_registration_with_incorrect_password_shows_error(driver, user_data):
    invalid_user = user_data.copy()
    invalid_user["password"] = "12345"

    open_register_page(driver)
    fill_registration_form(driver, invalid_user)
    submit_registration(driver)

    error = wait_for_visibility(driver, RegisterPageLocators.INCORRECT_PASSWORD_ERROR)
    assert error.text == "Некорректный пароль"

