from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка 'Оформить заказ' / 'Войти в аккаунт'
    ORDER_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_large")]'

    BUILDER_LINK = By.LINK_TEXT, 'Конструктор'
    BUILDER_HEADER = By.XPATH, './/h1[text()="Соберите бургер"]'

    ORDER_FEED_LINK = By.LINK_TEXT, 'Лента Заказов'

    FIRST_BUN = By.XPATH, './/a[contains(@href, "/ingredient/")][1]'
    INGREDIENT_HEADER_WINDOW = By.XPATH, './/h2[text()="Детали ингредиента"]'

    # Кнопка закрывающая окно деталей ингредиента
    CLOSE_WINDOW_INGREDIENT_BUTTON = By.XPATH, './/button[contains(@class, "Modal_modal__close_modified__3V5XS")][1]'

    # TOP_BUN = By.XPATH, './/div[contains(@class, "constructor-element_pos_top")]'  # Верхняя булка в конструкторе
    # TOP_BUN_PRICE = By.XPATH, './/span[contains(@class, "constructor-element__price")][1]'  # Цена верхней булки в собранном бургере

    DROP_BASKET_AREA = By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]'

    BUN_COUNTER = By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]'

    ORDER_NUMBER = By.XPATH, './/h2[contains(@class, "title_shadow__3ikwq")]'
