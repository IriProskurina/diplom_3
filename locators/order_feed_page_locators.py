from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    TITLE_LOCATOR = By.XPATH, "//*[contains(@class, 'text') and text()='Лента заказов']"  # заголовок
    ORDER_LOCATOR = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][1]/a"  # первый заказ в ленте
    ORDER_NUMBER_FROM_FEED_LOCATOR = \
        (By.XPATH,
         "//li[1]//*[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits')]")  # номер первого заказа в ленте
    ORDER_NUMBER_FROM_DETAILS_LOCATOR = \
        (By.XPATH,
         "//*[contains(@class, 'Modal_orderBox')]/p[contains(@class, 'text_type_digits')]")  # номер заказа в модальном окне
    SPECIFIC_ORDER_NUMBER_LOCATOR = (By.XPATH, "//*[text()='{}']")  # номер заказа из аккаунта
    COMPLETED_ORDERS_LOCATOR = \
        (By.XPATH,
         "//*[@class='text text_type_main-medium' and text()='{}']//following-sibling::p")  # счетчики завершенные заказов
    IN_PROGRESS_ORDER_LOCATOR = By.XPATH, "//*[contains(@class, 'OrderFeed_orderListReady')]/li"  # заказы в работе
