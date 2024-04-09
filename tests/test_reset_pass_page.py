import time

import pytest

import data


class TestLoginPage:
    def test_reset_password_turn_page_success(self, reset_pass_page):
        reset_pass_page.click_on_reset_password()

        assert reset_pass_page.get_text_from_header_reset_password_page() == 'Восстановление пароля'

    def test_reset_password_input_email_success(self, reset_pass_page):
        reset_pass_page.click_on_reset_password()
        reset_pass_page.fill_email_field(data.TEST_USER_EMAIL)
        reset_pass_page.click_on_reset_button()

        assert reset_pass_page.return_secret_key_field_text() == 'Введите код из письма'

    def test_hide_and_show_password_success(self, reset_pass_page):
        reset_pass_page.click_on_reset_password()
        reset_pass_page.fill_email_field(data.TEST_USER_EMAIL)
        reset_pass_page.click_on_reset_button()
        reset_pass_page.fill_password_field(data.TEST_USER_PASS)

        assert reset_pass_page.return_tipe_field() == 'text'
