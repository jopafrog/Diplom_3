import allure
from locators.login_page_locators import LoginPageLocators
from locators.reset_pass_page_locators import ResetPassPageLocators
from pages.base_page import BasePage


class ResetPassPage(BasePage):
    @allure.step('Заполнить поле email')
    def fill_email_field(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнить поле пароль')
    def fill_password_field(self, password):
        self.send_keys(LoginPageLocators.PASS_INPUT, password)

    @allure.step('Нажать на кнопку Восстановить пароль')
    def click_on_reset_button(self):
        self.click_on_element(ResetPassPageLocators.RESET_BUTTON)

    @allure.step('Нажать на ссылку для перехода на форму восстановления пароля')
    def click_on_reset_password(self):
        self.click_on_element(ResetPassPageLocators.RESET_PASS_LINK)

    @allure.step('Получить заголовок формы восстановления пароля')
    def get_text_from_header_reset_password_page(self):
        self.find_element_with_wait(ResetPassPageLocators.RESET_PASS_HEADER)
        return self.get_text_from_element(ResetPassPageLocators.RESET_PASS_HEADER)

    @allure.step('Получить текст в поле "введите код из письма"')
    def return_secret_key_field_text(self):
        return self.get_text_from_element(ResetPassPageLocators.SECRET_KEY_FIELD)

    @allure.step('Вернуть тип поля, в которое введен пароль')
    def return_tipe_field(self):
        self.click_on_element(ResetPassPageLocators.SHOW_PASS_BUTTON)
        return self.get_attribute_value(LoginPageLocators.PASS_INPUT, 'type')
