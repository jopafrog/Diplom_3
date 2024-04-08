import pytest

import data
from pages.login_page import LoginPage


class TestLoginPage:
    def test_login(self, driver):
        driver.get(data.LOGIN_PAGE)
        login_page = LoginPage(driver)

        login_page.fill_email_field(data.TEST_USER_EMAIL)
        login_page.fill_password_field(data.TEST_USER_PASS)
