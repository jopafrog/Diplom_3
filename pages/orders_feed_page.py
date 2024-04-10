from locators.orders_feed_locators import OrdersFeedLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    def click_on_first_order(self):
        self.click_on_element(OrdersFeedLocators.FIRST_ORDER)

    def order_window_open(self):
        element = self.get_attribute_value(OrdersFeedLocators.ORDER_WINDOW, 'class')
        if 'opened' in element:
            return True
        else:
            return False

    def close_details_order_window(self):
        self.click_on_element(OrdersFeedLocators.CLOSE_WINDOW_ORDER_BUTTON)
