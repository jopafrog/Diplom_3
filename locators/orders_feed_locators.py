from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    ORDER_FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'

    FIRST_ORDER = By.XPATH, './/a[contains(@class, "OrderHistory_link__1iNby")][1]'
    COMPOSITION_ORDER = By.XPATH, './/p[contains(@class, "text_type_main-medium mb-8")]'
    ORDER_WINDOW = By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section'

    CLOSE_WINDOW_ORDER_BUTTON = By.XPATH, './/section[contains(@class, "Modal_modal_opened__3ISw4")]//button'

