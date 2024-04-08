from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def fill_email_field(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.send_keys(LoginPageLocators.PASS_INPUT, password)
