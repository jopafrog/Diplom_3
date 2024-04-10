import pytest
from selenium import webdriver
import data
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.profile_page import ProfilePage
from pages.reset_pass_page import ResetPassPage


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif 'firefox' in request.param:
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
# @allure.title('Переход на главную и создание объекта MainPage')
def reset_pass_page(driver):
    driver.get(data.LOGIN_PAGE)
    return ResetPassPage(driver)


@pytest.fixture(scope='function')
# @allure.title('Переход на главную и создание объекта MainPage')
def profile_page(driver):
    driver.get(data.MAIN_PAGE)

    profile_page = ProfilePage(driver)
    profile_page.click_on_link_profile()
    profile_page.enter_profile(email=data.TEST_USER_EMAIL, password=data.TEST_USER_PASS)

    return profile_page


@pytest.fixture(scope='function')
# @allure.title('Переход на главную и создание объекта MainPage')
def main_page(driver):
    driver.get(data.MAIN_PAGE)
    return MainPage(driver)


@pytest.fixture(scope='function')
# @allure.title('Переход на главную и создание объекта MainPage')
def main_page_authorization(driver):
    driver.get(data.MAIN_PAGE)

    profile_page = ProfilePage(driver)
    profile_page.click_on_link_profile()
    profile_page.enter_profile(email=data.TEST_USER_EMAIL, password=data.TEST_USER_PASS)

    return MainPage(driver)


@pytest.fixture(scope='function')
# @allure.title('Переход на главную и создание объекта MainPage')
def orders_feed_page(driver):
    driver.get(data.ORDER_FEED_PAGE)
    return OrdersFeedPage(driver)
