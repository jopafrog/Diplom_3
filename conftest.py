import pytest
from selenium import webdriver


# @pytest.fixture(scope='function')
# @allure.title('Запуск драйвера (FireFox)')
def driver_fox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    driver_firefox = webdriver.Firefox(options=options)

    return driver_firefox
    # yield driver_fox

    # driver_fox.quit()


# @pytest.fixture(scope='function')
# @allure.title('Запуск драйвера (FireFox)')
def driver_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")

    driver_chrm = webdriver.Chrome(options=options)
    return driver_chrm
    #yield driver_chrome

    #driver_chrome.quit()


@pytest.fixture(scope='function', params=[driver_fox(), driver_chrome()])
def driver(request):
    driver = request.param

    yield driver

    driver.quit()
