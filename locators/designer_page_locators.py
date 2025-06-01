from selenium.webdriver.common.by import By


class DesignerPageLocators:
    TITLE_LOCATOR = (
        By.XPATH, "//*[contains(@class, 'text') and text()='Соберите бургер']")  # заголовок конструктора
    MODAL_TITLE_LOCATOR = (
        By.XPATH, "//*[contains(@class, 'Modal_modal') and text()='Детали ингредиента']")  # заголовок модального окна
    MODAL_CLOSE_BUTTON_LOCATOR = (
        By.XPATH, "//*[contains(@class, 'Modal_modal__close')]")  # крестик модального окна
    OPEN_MODAL_WINDOW_LOCATOR = (
        By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")  # открытое модальное окно
    INGREDIENT_LOCATOR = (
        By.XPATH,
        "//*[contains(@class, 'BurgerIngredient_ingredient__text') and text()='Соус Spicy-X']/parent::*")  # ингредиент
    BUN_LOCATOR = (By.XPATH, "//*[contains(@class, 'BurgerIngredient_ingredient__text') and text()='Флюоресцентная булка R2-D3']/parent::*")
    COUNTER_INGREDIENT_LOCATOR = (
        By.XPATH, "//*[contains(@class, 'BurgerIngredient_ingredient__text') and text()='Соус Spicy-X']/parent::*//p[contains(@class, 'counter_counter__num')]")  # счетчик ингредиента
    DROP_ZONE_LOCATOR = (
        By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")  # корзина
    MAKE_ORDER_BUTTON_LOCATOR = By.XPATH, "//*[contains(@class, 'button_button_size_large')]"  # кнопка "Сделать заказ"
    ORDER_CONFIRMATION_TEXT_LOCATOR = (
        By.XPATH,
        "//p[contains(@class, 'text_type_main-small') and text() = 'Ваш заказ начали готовить']")  # текст подтверждения заказа
    LOADER_LOCATOR = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"
    BASKET_LOCATOR = ("xpath", "//div[@class='BurgerConstructort']")
    ORDER_CONFIRM_LOCATOR = ("XPATH", "//div[contains(text(), 'Заказ оформлен')]")
    MODAL_WINDOW_LOCATOR = (By.ID, "ingredient-modal")