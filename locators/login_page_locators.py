from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_BUTTON_LOCATOR = (
        By.XPATH, "//*[contains(@class, 'Auth_link') and text()='Восстановить пароль']")  # кнопка "Восстановить пароль"
    HEADING_TEXT_LOCATOR = By.XPATH, "//*[contains(@class, 'Auth_login')]/h2"  # заголовок "Вход"
    PASSWORD_LOCATOR = By.NAME, "Пароль"  # поле Пароль
    EMAIL_LOCATOR = By.NAME, "name"  # поле Имя
    ENTER_BUTTON = By.XPATH, "//*[text()='Войти']"  # кнопка "Войти"
