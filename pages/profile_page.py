from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.reset_pass_page_locators import ResetPassPageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def click_on_link_profile(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON)
        self.click_on_element(ProfilePageLocators.PROFILE_LINK)

    def click_on_history_orders(self):
        self.click_on_element(ProfilePageLocators.HISTORY_LINK)

    def click_on_logout_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    def enter_profile(self, email, password):
        self.send_keys(ResetPassPageLocators.EMAIL_INPUT, email)
        self.send_keys(ResetPassPageLocators.PASS_INPUT, password)
        self.click_on_element(ResetPassPageLocators.RESET_BUTTON)

    def get_user_name_in_profile(self):
        return self.get_attribute_value(ProfilePageLocators.NAME_FIELD, 'value')

    def get_status_order(self):
        return self.get_text_from_element(ProfilePageLocators.ORDER_DONE)

    def get_header_login_page(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_HEADER)
