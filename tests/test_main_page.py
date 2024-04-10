

class TestMainPage:
    def test_open_builder_page_success(self, main_page):
        main_page.click_on_order_feed_link()
        main_page.click_on_builder_link()

        assert main_page.get_header_builder() == 'Соберите бургер'

    def test_open_order_feed_success(self, main_page):
        main_page.click_on_order_feed_link()

        assert main_page.get_header_order_feed() == 'Лента заказов'

    def test_open_details_ingredient_window(self, main_page):
        main_page.click_on_first_ingredient()

        assert main_page.get_header_ingredient_window() == 'Детали ингредиента'

    def test_close_ingredient_details_window_success(self, main_page):
        main_page.click_on_first_ingredient()
        main_page.close_ingredient_details_window()

        assert main_page.find_ingredient_details_window() is False

    def test_drag_and_drop_top_bun_price_not_zero(self, main_page):
        main_page.drag_bun_and_drop_in_order()

        assert main_page.get_bun_counter() == '2'

    def test_place_order_authorization_user_success(self, main_page_authorization):
        main_page_authorization.drag_bun_and_drop_in_order()
        main_page_authorization.click_on_order_button()

        assert main_page_authorization.get_order_number() != 0

