from helpers import (
    open_main_page,
    switch_to_buns,
    switch_to_fillings,
    switch_to_sauces,
    wait_for_visibility,
)
from locators import ConstructorPageLocators


def test_switch_to_sauces_tab(driver):
    open_main_page(driver)
    switch_to_sauces(driver)

    wait_for_visibility(driver, ConstructorPageLocators.ACTIVE_SAUCES_TAB)


def test_switch_to_fillings_tab(driver):
    open_main_page(driver)
    switch_to_fillings(driver)

    wait_for_visibility(driver, ConstructorPageLocators.ACTIVE_FILLINGS_TAB)


def test_switch_to_buns_tab(driver):
    open_main_page(driver)
    switch_to_sauces(driver)
    switch_to_buns(driver)

    wait_for_visibility(driver, ConstructorPageLocators.ACTIVE_BUNS_TAB)
