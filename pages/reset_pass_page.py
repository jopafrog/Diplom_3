from locators.reset_pass_page_locators import ResetPassPageLocators
from pages.base_page import BasePage


class ResetPassPage(BasePage):
    def fill_email_field(self, email):
        self.send_keys(ResetPassPageLocators.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.send_keys(ResetPassPageLocators.PASS_INPUT, password)

    def click_on_reset_button(self):
        self.click_on_element(ResetPassPageLocators.RESET_BUTTON)

    def click_on_reset_password(self):
        self.click_on_element(ResetPassPageLocators.RESET_PASS_LINK)

    def get_text_from_header_reset_password_page(self):
        self.find_element_with_wait(ResetPassPageLocators.RESET_PASS_HEADER)
        return self.get_text_from_element(ResetPassPageLocators.RESET_PASS_HEADER)

    def return_secret_key_field_text(self):
        return self.get_text_from_element(ResetPassPageLocators.SECRET_KEY_FIELD)

    def return_tipe_field(self):
        self.click_on_element(ResetPassPageLocators.SHOW_PASS_BUTTON)
        return self.get_attribute_value(ResetPassPageLocators.PASS_INPUT, 'type')
