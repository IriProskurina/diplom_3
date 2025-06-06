import allure
from pages.base_page import BasePage
from locators.designer_page_locators import DesignerPageLocators
from data import Links

class DesignerPage(BasePage):

    @allure.step('Открытие страницы конструктора')
    def open_design_page(self):
        self.open_url(Links.MAIN_LINK)

    @allure.step('Открытие детали ингредиента по локатору')
    def open_ingredient_details(self):
        self.click_to_element(DesignerPageLocators.INGREDIENT_LOCATOR)

    @allure.step('Закрытие окна детали ингредиента')
    def close_ingredient_details(self):
        self.click_to_element(DesignerPageLocators.MODAL_CLOSE_BUTTON_LOCATOR)

    @allure.step('Получение заголовка конструктора')
    def get_title(self):
        return self.get_text_from_element(DesignerPageLocators.TITLE_LOCATOR)

    @allure.step('Получение заголовка модального окна ингредиента')
    def get_ingredient_window_title(self):
        return self.get_text_from_element(DesignerPageLocators.MODAL_TITLE_LOCATOR)

    @allure.step('Проверка отсутствия класса opened у модального окна ингредиента')
    def check_visibility_of_modal_title(self):
        modal_title_attr = self.get_attribute_of_element(
            DesignerPageLocators.MODAL_TITLE_LOCATOR, 'class')
        return 'opened' not in modal_title_attr

    @allure.step('Drag&Drop ингредиента по локатору {ingredient_locator} в область корзины')
    def drag_ingredient_to_basket(self, ingredient_locator):
        self.drag_and_drop_element(ingredient_locator, DesignerPageLocators.DROP_ZONE_LOCATOR)

    @allure.step('Получение значения счетчика ингредиентов')
    def get_ingredient_count(self):
        return self.get_text_from_element(DesignerPageLocators.COUNTER_INGREDIENT_LOCATOR)

    @allure.step('Клик по кнопке оформить заказ')
    def click_to_make_order_button(self):
        self.click_to_element(DesignerPageLocators.MAKE_ORDER_BUTTON_LOCATOR)

    @allure.step('Добавление булки и ингредиента в корзину и оформление заказа')
    def make_order_with_bun_and_ingredient(self):
        self.drag_ingredient_to_basket(DesignerPageLocators.BUN_LOCATOR)
        self.drag_ingredient_to_basket(DesignerPageLocators.INGREDIENT_LOCATOR)
        self.click_to_make_order_button()

    @allure.step('Проверка появления записи о подтверждении заказа')
    def check_order_confirmation(self):
        return self.find_element_with_waiting(
            DesignerPageLocators.ORDER_CONFIRMATION_TEXT_LOCATOR).is_displayed()


