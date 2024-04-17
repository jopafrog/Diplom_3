import allure
import data
from pages.profile_page import ProfilePage


class TestProfilePage:
    @allure.title('Проверка открытия Личного кабинета')
    def test_open_profile_success(self, driver):
        driver.get(data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=data.TEST_USER_EMAIL, password=data.TEST_USER_PASS)
        profile_page.click_on_link_profile()

        assert profile_page.get_user_name_in_profile() == data.TEST_USER_NAME

    @allure.title('Проверка открытия Истории заказов')
    def test_open_history_order_success(self, driver):
        driver.get(data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=data.TEST_USER_EMAIL, password=data.TEST_USER_PASS)
        profile_page.click_on_link_profile()
        profile_page.click_on_history_orders()

        assert profile_page.get_status_order() == 'Выполнен'

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_profile_success(self, driver):
        driver.get(data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=data.TEST_USER_EMAIL, password=data.TEST_USER_PASS)
        profile_page.click_on_link_profile()
        profile_page.click_on_logout_button()

        assert profile_page.get_header_login_page() == 'Вход'
