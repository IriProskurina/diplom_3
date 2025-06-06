from selenium.webdriver.common.by import By


class HeaderPageLocators:
    ACCOUNT_BUTTON_LOCATOR = \
        (By.XPATH,
         "//*[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']")  # кнопка Личный кабинет
    DESIGNER_BUTTON_LOCATOR = \
        (By.XPATH, "//*[contains(@class, 'AppHeader_header') and text()='Конструктор']")  # кнопка Конструктор
    ORDER_FEED_BUTTON_LOCATOR = \
        (By.XPATH, "//*[contains(@class, 'AppHeader_header') and text()='Лента Заказов']")  # кнопка Лента заказов
