from selenium.webdriver.common.by import By


class ResetPassPageLocators:
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/parent::div/input'
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/parent::div/input'

    LOGIN_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_medium")]'
    RESET_PASS_LINK = By.LINK_TEXT, 'Восстановить пароль'
    RESET_PASS_HEADER = By.XPATH, './/h2[text()="Восстановление пароля"]'

    SECRET_KEY_FIELD = By.XPATH, './/label[text()="Введите код из письма"]'
    SECRET_KEY_INPUT = By.XPATH, './/label[text()="Введите код из письма"]/parent::div/input'
