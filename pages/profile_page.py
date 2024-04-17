import allure
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.reset_pass_page_locators import ResetPassPageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Нажать на ссылку Личного кабинета')
    def click_on_link_profile(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON)
        self.click_on_element(ProfilePageLocators.PROFILE_LINK)

    @allure.step('Нажать на Историю заказов')
    def click_on_history_orders(self):
        self.click_on_element(ProfilePageLocators.HISTORY_LINK)

    @allure.step('Нажать на кнопку выхода из аккаунта')
    def click_on_logout_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Авторизация на сайте')
    def enter_profile(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASS_INPUT, password)
        self.click_on_element(ResetPassPageLocators.RESET_BUTTON)

    @allure.step('Получить имя пользователя из поля, в Личном кабинете')
    def get_user_name_in_profile(self):
        return self.get_attribute_value(ProfilePageLocators.NAME_FIELD, 'value')

    @allure.step('Получить статус заказа в окне заказа (История заказов)')
    def get_status_order(self):
        return self.get_text_from_element(ProfilePageLocators.ORDER_DONE)

    @allure.step('Получить заголовок страницы входа')
    def get_header_login_page(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_HEADER)
