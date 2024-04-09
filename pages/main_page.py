import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_order_feed_link(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    def click_on_builder_link(self):
        self.click_on_element(MainPageLocators.BUILDER_LINK)

    def get_header_builder(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        return self.get_text_from_element(MainPageLocators.BUILDER_HEADER)

    def get_header_order_feed(self):
        self.find_element_with_wait(MainPageLocators.ORDER_FEED_HEADER)
        return self.get_text_from_element(MainPageLocators.ORDER_FEED_HEADER)

    def click_on_first_ingredient(self):
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT_LINK)

    def get_header_ingredient_window(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_HEADER_WINDOW)

    def close_ingredient_details_window(self):
        self.click_on_element(MainPageLocators.CLOSE_WINDOW_INGREDIENT_BUTTON)

    def find_ingredient_details_window(self):
        return self.element_exist(MainPageLocators.INGREDIENT_HEADER_WINDOW)
