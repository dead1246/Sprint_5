from helpers import (
    login_user,
    open_login_page,
    open_main_page,
    open_personal_account,
    wait_for_clickable,
    wait_for_url,
    wait_for_visibility,
)
from locators import AccountPageLocators, LoginPageLocators, MainPageLocators


class TestProfileNavigation:
    def test_personal_account_navigation(self, driver, registered_user):
        open_main_page(driver)
        wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        assert wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING).is_displayed()
        login_user(driver, registered_user["email"], registered_user["password"])
        open_personal_account(driver)

        assert "/account" in driver.current_url

    def test_transition_from_personal_account_to_constructor_by_constructor_link(
        self, driver, registered_user
    ):
        open_login_page(driver)
        login_user(driver, registered_user["email"], registered_user["password"])
        open_personal_account(driver)
        wait_for_clickable(driver, MainPageLocators.CONSTRUCTOR_LINK).click()

        assert wait_for_visibility(driver, MainPageLocators.MAIN_HEADING).is_displayed()
        wait_for_url(driver, "/")
        assert driver.current_url.endswith("/")

    def test_transition_from_personal_account_to_constructor_by_logo(
        self, driver, registered_user
    ):
        open_login_page(driver)
        login_user(driver, registered_user["email"], registered_user["password"])
        open_personal_account(driver)
        wait_for_clickable(driver, MainPageLocators.STELLAR_BURGERS_LOGO).click()

        assert wait_for_visibility(driver, MainPageLocators.MAIN_HEADING).is_displayed()
        wait_for_url(driver, "/")
        assert driver.current_url.endswith("/")

    def test_logout_from_personal_account(self, driver, registered_user):
        open_login_page(driver)
        login_user(driver, registered_user["email"], registered_user["password"])
        open_personal_account(driver)
        wait_for_clickable(driver, AccountPageLocators.LOGOUT_BUTTON).click()

        wait_for_url(driver, "/login")
        assert wait_for_visibility(driver, LoginPageLocators.LOGIN_HEADING).is_displayed()
        assert "/login" in driver.current_url
