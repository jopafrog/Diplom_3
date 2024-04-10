from locators.main_page_locators import MainPageLocators
from locators.orders_feed_locators import OrdersFeedLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_order_feed_link(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    def click_on_builder_link(self):
        self.click_on_element(MainPageLocators.BUILDER_LINK)

    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    def get_header_builder(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        return self.get_text_from_element(MainPageLocators.BUILDER_HEADER)

    def get_header_order_feed(self):
        self.find_element_with_wait(OrdersFeedLocators.ORDER_FEED_HEADER)
        return self.get_text_from_element(OrdersFeedLocators.ORDER_FEED_HEADER)

    def click_on_first_ingredient(self):
        self.click_on_element(MainPageLocators.FIRST_BUN)

    def get_header_ingredient_window(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_HEADER_WINDOW)

    def close_ingredient_details_window(self):
        self.click_on_element(MainPageLocators.CLOSE_WINDOW_INGREDIENT_BUTTON)

    def find_ingredient_details_window(self):
        return self.element_exist(MainPageLocators.INGREDIENT_HEADER_WINDOW)

    def drag_bun_and_drop_in_order(self):
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.DROP_BASKET_AREA)

    def get_bun_counter(self):
        return self.get_text_from_element(MainPageLocators.BUN_COUNTER)

    def get_order_number(self):
        return int(self.get_text_from_element(MainPageLocators.ORDER_NUMBER))
