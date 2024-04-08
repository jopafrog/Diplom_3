from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/parent::div/input'
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/parent::div/input'
