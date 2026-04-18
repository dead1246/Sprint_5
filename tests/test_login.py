from helpers import (
    login_user,
    open_login_page,
    open_main_page,
    open_register_page,
    wait_for_clickable,
    wait_for_visibility,
)
from locators import (
    ForgotPasswordPageLocators,
    LoginPageLocators,
    MainPageLocators,
    RegisterPageLocators,
)


class TestLogin:
    def test_login_from_main_page_button(self, driver, registered_user):
        open_main_page(driver)
        wait_for_clickable(driver, MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        login_user(driver, registered_user["email"], registered_user["password"])

        assert wait_for_visibility(driver, MainPageLocators.MAIN_HEADING).is_displayed()

    def test_login_from_personal_account_button(self, driver, registered_user):
        open_main_page(driver)
        wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        login_user(driver, registered_user["email"], registered_user["password"])

        assert wait_for_visibility(driver, MainPageLocators.MAIN_HEADING).is_displayed()

    def test_login_from_registration_form(self, driver, registered_user):
        open_register_page(driver)
        wait_for_clickable(driver, RegisterPageLocators.LOGIN_LINK).click()

        login_user(driver, registered_user["email"], registered_user["password"])

        assert wait_for_visibility(driver, MainPageLocators.MAIN_HEADING).is_displayed()

    def test_login_from_forgot_password_form(self, driver, registered_user):
        open_login_page(driver)
        wait_for_clickable(driver, LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        assert wait_for_visibility(
            driver, ForgotPasswordPageLocators.FORGOT_PASSWORD_HEADING
        ).is_displayed()
        wait_for_clickable(driver, ForgotPasswordPageLocators.LOGIN_LINK).click()

        login_user(driver, registered_user["email"], registered_user["password"])

        assert wait_for_visibility(driver, MainPageLocators.MAIN_HEADING).is_displayed()
