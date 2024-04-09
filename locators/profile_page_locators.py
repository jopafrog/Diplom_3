from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = By.LINK_TEXT, 'Личный Кабинет'
    HISTORY_LINK = By.LINK_TEXT, 'История заказов'
    LOGOUT_BUTTON = By.XPATH, './/button[contains(@class, "Account_button")]'  # Кнопка выхода из аккаунта

    NAME_FIELD = By.XPATH, './/label[text()="Имя"]/parent::div/input'  # Поле с именем пользователя
    ORDER_NUMBER = By.XPATH, './/p[contains(@class, "text text_type_digits-default")][1]'
    ORDER_DONE = By.XPATH, './/p[contains(@class, "OrderHistory_visible__19YMB")][1]'  # Кнопка отображения пароля
