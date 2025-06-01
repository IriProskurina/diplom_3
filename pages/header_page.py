import allure

from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_to_account_button(self):
        self.click_to_element(HeaderPageLocators.ACCOUNT_BUTTON_LOCATOR)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_to_designer_button(self):
        self.click_to_element(HeaderPageLocators.DESIGNER_BUTTON_LOCATOR)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_to_order_feed_button(self):
        self.click_to_element(HeaderPageLocators.ORDER_FEED_BUTTON_LOCATOR)