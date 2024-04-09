

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
