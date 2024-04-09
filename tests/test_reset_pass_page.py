import time

import pytest

import data
from locators.main_page_locators import MainPageLocators
from pages.reset_pass_page import ResetPassPage


class TestLoginPage:
    def test_login(self, driver):
        driver.get(data.LOGIN_PAGE)
        login_page = ResetPassPage(driver)

        login_page.fill_email_field(data.TEST_USER_EMAIL)
        login_page.fill_password_field(data.TEST_USER_PASS)

        login_page.click_on_login_button()
        login_page.find_element_with_wait(MainPageLocators.PLACE_ORDER_BUTTON)

        assert driver.current_url == data.MAIN_PAGE

    def test_reset_password_turn_page_success(self, driver):
        driver.get(data.LOGIN_PAGE)
        login_page = ResetPassPage(driver)

        login_page.click_on_reset_password()

        assert login_page.get_text_from_header_reset_password_page() == 'Восстановление пароля'

    def test_reset_password_input_email_success(self, driver):
        driver.get(data.LOGIN_PAGE)
        login_page = ResetPassPage(driver)

        login_page.click_on_reset_password()
        field_text = login_page.reset_password_and_return_secret_key_field_text(data.TEST_USER_EMAIL)

        assert field_text == 'Введите код из письма'
