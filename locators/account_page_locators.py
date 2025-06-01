from selenium.webdriver.common.by import By


class AccountPageLocators:
    NAME_LOCATOR = By.NAME, "Name"  # поле Имя
    HISTORY_BUTTON_LOCATOR = By.XPATH, "//*[text()='История заказов']"  # кнопка История заказов
    EXIT_BUTTON_LOCATOR = By.XPATH, "//*[text()='Выход']"  # кнопка "Выход"
    ORDER_NUMBER_LOCATOR = (
        By.XPATH,
        "//li[1]//*[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits')]")  # номер заказа
