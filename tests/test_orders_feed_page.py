class TestOrdersFeedPage:
    def test_open_details_order_window_success(self, orders_feed_page):
        orders_feed_page.click_on_first_order()

        assert orders_feed_page.order_window_open() is True

    def test_close_details_order_window_success(self, orders_feed_page):
        orders_feed_page.click_on_first_order()
        orders_feed_page.close_details_order_window()

        assert orders_feed_page.order_window_open() is False
