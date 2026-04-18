from helpers import (
    open_main_page,
    switch_to_buns,
    switch_to_fillings,
    switch_to_sauces,
)


class TestConstructor:
    def test_switch_to_sauces_tab(self, driver):
        open_main_page(driver)
        section = switch_to_sauces(driver)

        assert section.is_displayed()

    def test_switch_to_fillings_tab(self, driver):
        open_main_page(driver)
        section = switch_to_fillings(driver)

        assert section.is_displayed()

    def test_switch_to_buns_tab(self, driver):
        open_main_page(driver)
        switch_to_sauces(driver)
        section = switch_to_buns(driver)

        assert section.is_displayed()
