from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка 'Оформить заказ' / 'Войти в аккаунт'
    PLACE_ORDER_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_large")]'

    BUILDER_LINK = By.LINK_TEXT, 'Конструктор'
    BUILDER_HEADER = By.XPATH, './/h1[text()="Соберите бургер"]'

    ORDER_FEED_LINK = By.LINK_TEXT, 'Лента Заказов'
    ORDER_FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'

    FIRST_INGREDIENT_LINK = By.XPATH, './/a[contains(@href, "/ingredient/")][1]'
    INGREDIENT_HEADER_WINDOW = By.XPATH, './/h2[text()="Детали ингредиента"]'

    CLOSE_WINDOW_INGREDIENT_BUTTON = By.XPATH, './/button[contains(@class, "Modal_modal__close_modified__3V5XS")][1]'
