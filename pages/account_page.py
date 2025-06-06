import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data import Links


class AccountPage(BasePage):
    @allure.step('Получаем имя пользователя')
    def get_name(self):
        return self.get_attribute_of_element(AccountPageLocators.NAME_LOCATOR, "value")

    @allure.step('Нажимаем на историю заказов пользователя')
    def click_to_order_history_button(self):
        self.click_to_element(AccountPageLocators.HISTORY_BUTTON_LOCATOR)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_to_exit_button(self):
        self.click_to_element(AccountPageLocators.EXIT_BUTTON_LOCATOR)

    @allure.step('Проверяем, что кнопка "История заказов" активна')
    def check_active_history_button(self):
        active_button_class = "Account_link_active"
        selected_button_class = self.get_attribute_of_element(AccountPageLocators.HISTORY_BUTTON_LOCATOR, "class")
        return active_button_class in selected_button_class

    @allure.step('Проверяем, что текущий url равен адресу истории заказов пользователя')
    def check_order_history_url(self):
        return self.get_url() == Links.ORDER_HISTORY_LINK

    @allure.step('Получаем заказ пользователя в истории заказов')
    def get_order_number(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_NUMBER_LOCATOR)
