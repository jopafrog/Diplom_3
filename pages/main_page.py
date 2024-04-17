import allure
from locators.main_page_locators import MainPageLocators
from locators.orders_feed_locators import OrdersFeedLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на ссылку "Лента заказов"')
    def click_on_order_feed_link(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Нажать на ссылку "Конструктор"')
    def click_on_builder_link(self):
        self.click_on_element(MainPageLocators.BUILDER_LINK)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить заголовок страницы Конструктор')
    def get_header_builder(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        return self.get_text_from_element(MainPageLocators.BUILDER_HEADER)

    @allure.step('Получить заголовок страницы Лента заказов')
    def get_header_order_feed(self):
        self.find_element_with_wait(OrdersFeedLocators.ORDER_FEED_HEADER)
        return self.get_text_from_element(OrdersFeedLocators.ORDER_FEED_HEADER)

    @allure.step('Нажать на первый ингредиент в конструкторе')
    def click_on_first_ingredient(self):
        self.click_on_element(MainPageLocators.FIRST_BUN)

    @allure.step('Получить заголовок окна Детали ингредиента')
    def get_header_ingredient_window(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_WINDOW_HEADER)

    @allure.step('Нажать на крестик в окне Детали ингредиента')
    def close_ingredient_details_window(self):
        self.click_on_element(MainPageLocators.CLOSE_WINDOW_INGREDIENT_BUTTON)

    @allure.step('Проверка наличия окна Детали ингредиента')
    def find_ingredient_details_window(self):
        return self.element_exist(MainPageLocators.INGREDIENT_WINDOW_HEADER)

    @allure.step('Перетащить булку из конструктора в заказ')
    def drag_bun_and_drop_in_order(self):
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.DROP_BASKET_AREA)

    @allure.step('Получить счетчик булки в конструкторе')
    def get_bun_counter(self):
        return self.get_text_from_element(MainPageLocators.BUN_COUNTER)

    @allure.step('Получить номер оформленного заказа')
    def get_order_number(self):
        return int(self.get_text_from_element(MainPageLocators.ORDER_NUMBER))
