from locators.reset_pass_page_locators import ResetPassPageLocators
from pages.base_page import BasePage


class ResetPassPage(BasePage):
    def fill_email_field(self, email):
        self.send_keys(ResetPassPageLocators.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.send_keys(ResetPassPageLocators.PASS_INPUT, password)

    def click_on_login_button(self):
        self.click_on_element(ResetPassPageLocators.LOGIN_BUTTON)

    def click_on_reset_password(self):
        self.click_on_element(ResetPassPageLocators.RESET_PASS_LINK)

    def get_text_from_header_reset_password_page(self):
        self.find_element_with_wait(ResetPassPageLocators.RESET_PASS_HEADER)
        return self.get_text_from_element(ResetPassPageLocators.RESET_PASS_HEADER)

    def reset_password_and_return_secret_key_field_text(self, email):
        self.send_keys(ResetPassPageLocators.EMAIL_INPUT, email)
        self.click_on_element(ResetPassPageLocators.LOGIN_BUTTON)

        return self.get_text_from_element(ResetPassPageLocators.SECRET_KEY_FIELD)
