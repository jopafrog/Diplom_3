from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка 'Оформить заказ' / 'Войти в аккаунт'
    ORDER_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_large")]'

    BUILDER_LINK = By.LINK_TEXT, 'Конструктор'
    BUILDER_HEADER = By.XPATH, './/h1[text()="Соберите бургер"]'

    ORDER_FEED_LINK = By.LINK_TEXT, 'Лента Заказов'

    # Первая булка в конструкторе
    FIRST_BUN = By.XPATH, '(.//a[contains(@href, "/ingredient/")])[1]'

    INGREDIENT_WINDOW_HEADER = By.XPATH, './/h2[text()="Детали ингредиента"]'

    # Кнопка закрывающая окно деталей ингредиента
    CLOSE_WINDOW_INGREDIENT_BUTTON = By.XPATH, './/button[contains(@class, "Modal_modal__close_modified__3V5XS")][1]'

    # Зона, куда перетаскиваются ингредиенты
    DROP_BASKET_AREA = By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]'

    # Счетчик добавленных булок(которые первые в списке)
    BUN_COUNTER = By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]'

    # Номер заказа, во всплывающем окне, при оформлении
    ORDER_NUMBER = By.XPATH, './/h2[contains(@class, "title_shadow__3ikwq")]'
