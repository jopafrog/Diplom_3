import allure


class TestOrdersFeedPage:
    @allure.title('Проверка открытия окна детализации заказа')
    def test_open_details_order_window_success(self, orders_feed_page):
        orders_feed_page.click_on_first_order()

        assert orders_feed_page.order_window_open() is True

    @allure.title('Проверка закрытия окна детализации заказа')
    def test_close_details_order_window_success(self, orders_feed_page):
        orders_feed_page.click_on_first_order()
        orders_feed_page.close_details_order_window()

        assert orders_feed_page.order_window_open() is False

    @allure.title('Проверка наличия последнего заказа пользователя в Ленте заказов')
    def test_check_order_user_in_orders_feed_success(self, orders_feed_page_authorize):
        orders_feed_page_authorize.create_order()
        orders_feed_page_authorize.close_details_order_window()
        order_number = orders_feed_page_authorize.get_lust_number_order()
        orders_feed_page_authorize.click_on_orders_feed()
        orders_feed_page_authorize.click_on_first_order()

        assert orders_feed_page_authorize.get_order_number_in_orders_feed() == order_number

    @allure.title('Проверка увеличения счетчика заказов за все время, при оформлении нового')
    def test_check_all_order_counter_increased(self, orders_feed_page_authorize):
        orders_feed_page_authorize.click_on_orders_feed()
        before_orders = orders_feed_page_authorize.get_all_orders_counter()

        orders_feed_page_authorize.click_on_builder()
        orders_feed_page_authorize.create_order()
        orders_feed_page_authorize.close_details_order_window()

        orders_feed_page_authorize.click_on_orders_feed()
        after_orders = orders_feed_page_authorize.get_all_orders_counter()

        assert int(before_orders) < int(after_orders)

    @allure.title('Проверка увеличения счетчика заказов за сегодня, при оформлении нового')
    def test_check_today_order_counter_increased(self, orders_feed_page_authorize):
        orders_feed_page_authorize.click_on_orders_feed()
        before_orders = orders_feed_page_authorize.get_today_orders_counter()

        orders_feed_page_authorize.click_on_builder()
        orders_feed_page_authorize.create_order()
        orders_feed_page_authorize.close_details_order_window()

        orders_feed_page_authorize.click_on_orders_feed()
        after_orders = orders_feed_page_authorize.get_today_orders_counter()

        assert int(before_orders) < int(after_orders)

    @allure.title('Проверка отображения нового заказа, что он находится "В работе"')
    def test_check_new_order_in_work_success(self, orders_feed_page_authorize):
        orders_feed_page_authorize.create_order()
        order_number = orders_feed_page_authorize.get_new_order_number()
        orders_feed_page_authorize.close_details_order_window()
        orders_feed_page_authorize.click_on_orders_feed()

        print(order_number)

        assert order_number in orders_feed_page_authorize.get_orders_in_work()
