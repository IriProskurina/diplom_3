from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    TITLE_LOCATOR = By.XPATH, "//*[contains(@class, 'Auth_login')]/h2"  # Заголовок "Восстановление пароля"
    EMAIL_LOCATOR = By.NAME, "name"  # поле e-mail
    # PASSWORD_LOCATOR = By.NAME, "//*[contains(@class, 'input_type_password')]"  # поле Пароль
    RECOVERY_BUTTON_LOCATOR = By.XPATH, "//*[contains(@class, 'button_button_size_medium')]"  # кнопка Восстановить
    KEY_PLACEHOLDER_LOCATOR = By.XPATH, "//*[text()='Введите код из письма']"  # плейсходер поля е-mail кода
    SHOW_HIDE_PASSWORD_ICON_LOCATOR = (
        By.XPATH, "//*[contains(@class, 'input__icon')]/child::*")  # иконка скрыть/показать пароль
    HIGHLIGHT_ACTIVE_PASSWORD_LOCATOR = (
        By.XPATH, "//*[contains(@class,'input_status_active')]")  # активная подсветка поля Пароль
