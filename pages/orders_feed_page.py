import allure
from locators.main_page_locators import MainPageLocators
from locators.orders_feed_locators import OrdersFeedLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    @allure.step('Нажать на ссылку Лента заказов')
    def click_on_orders_feed(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Нажать на ссылку Лента заказов, из Личного профиля')
    def go_to_orders_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Нажать на ссылку Конструктор')
    def click_on_builder(self):
        self.click_on_element(MainPageLocators.BUILDER_LINK)

    @allure.step('Нажать на первый заказ в Ленте')
    def click_on_first_order(self):
        self.click_on_element(OrdersFeedLocators.FIRST_ORDER)

    @allure.step('Проверка открыто ли окно заказа')
    def order_window_open(self):
        element = self.get_attribute_value(OrdersFeedLocators.ORDER_WINDOW, 'class')
        if 'opened' in element:
            return True
        else:
            return False

    @allure.step('Закрыть окно заказа')
    def close_details_order_window(self):
        self.click_on_element(OrdersFeedLocators.CLOSE_WINDOW_ORDER_BUTTON)

    @allure.step('Получить номер последнего сделанного заказа пользователем')
    def get_lust_number_order(self):
        self.click_on_element(ProfilePageLocators.PROFILE_LINK)
        self.click_on_element(ProfilePageLocators.HISTORY_LINK)
        return self.get_text_from_element(ProfilePageLocators.LAST_ORDER)

    @allure.step('Получить номер нового заказа')
    def get_new_order_number(self):
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Получить номер заказа в Лента заказов')
    def get_order_number_in_orders_feed(self):
        return self.get_text_from_element(OrdersFeedLocators.ORDER_NUMBER_IN_WINDOW)

    @allure.step('Создать заказ')
    def create_order(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.DROP_BASKET_AREA)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить значение счетчика заказов за все время')
    def get_all_orders_counter(self):
        self.find_element_with_wait(OrdersFeedLocators.ALL_ORDERS_COUNTER)
        return self.get_text_from_element(OrdersFeedLocators.ALL_ORDERS_COUNTER)

    @allure.step('Получить значение счетчика заказов за сегодня')
    def get_today_orders_counter(self):
        self.find_element_with_wait(OrdersFeedLocators.TODAY_ORDERS_COUNTER)
        return self.get_text_from_element(OrdersFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Получить список заказов в работе')
    def get_orders_in_work(self):
        self.find_element_with_wait(OrdersFeedLocators.EMPTY_ORDERS_IN_WORK)
        self.wait_disappear_element(OrdersFeedLocators.EMPTY_ORDERS_IN_WORK)
        return self.get_text_from_element(OrdersFeedLocators.ORDERS_IN_WORK)

    @allure.step('Ожидание формирования номера заказа')
    def wait_order_placed(self):
        self.find_element_with_wait(OrdersFeedLocators.ORDER_WINDOW_OPENED)
        self.wait_disappear_element(OrdersFeedLocators.ORDER_WINDOW_OPENED)
