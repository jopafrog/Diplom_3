from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    ORDER_FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'

    # Первый заказ в ленте заказов
    FIRST_ORDER = By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]'
    # COMPOSITION_ORDER = By.XPATH, './/p[contains(@class, "text_type_main-medium mb-8")]'
    ORDER_WINDOW = By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section'

    CLOSE_WINDOW_ORDER_BUTTON = By.XPATH, './/section[contains(@class, "Modal_modal_opened__3ISw4")]//button'

    ORDER_NUMBER_IN_WINDOW = By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]'

    # Счетчик "Выполнено за все время"
    ALL_ORDERS_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[1]'

    # Счетчик "Выполнено за сегодня"
    TODAY_ORDERS_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[last()]'

    # Заказы находящиеся в работе
    ORDERS_IN_WORK = By.XPATH, '(.//ul[contains(@class, "OrderFeed_orderListReady")]/li)[1]'
