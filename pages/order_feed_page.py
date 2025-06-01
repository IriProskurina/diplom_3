import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from helpers import format_locator
from data import Links


class OrderFeedPage(BasePage):
    @allure.step('Открываем страницу ленты заказов')
    def open_order_feed_page(self):
        self.open_url(Links.ORDER_FEED_LINK)

    @allure.step('Получаем заголовок страницы')
    def get_title(self):
        return self.get_text_from_element(OrderFeedPageLocators.TITLE_LOCATOR)

    @allure.step('Открываем детали заказа')
    def open_order_details(self):
        self.click_to_element(OrderFeedPageLocators.ORDER_LOCATOR)

    @allure.step('Получаем номер заказа из ленты')
    def get_order_number_from_feed(self):
        self.get_text_from_element(OrderFeedPageLocators.ORDER_NUMBER_FROM_FEED_LOCATOR)

    @allure.step('Получаем номер заказа из деталей заказа')
    def get_order_number_from_order_details(self):
        self.get_text_from_element(OrderFeedPageLocators.ORDER_NUMBER_FROM_DETAILS_LOCATOR)

    @allure.step('Скроллим ленту до нужного заказа')
    def scroll_to_order(self, order_number):
        order_locator = format_locator(OrderFeedPageLocators.SPECIFIC_ORDER_NUMBER_LOCATOR, order_number)
        self.scroll_to_element(order_locator)

    @allure.step('Получаем номер определенного заказа')
    def get_specific_order_from_order_feed(self, order_number):
        order_locator = format_locator(OrderFeedPageLocators.SPECIFIC_ORDER_NUMBER_LOCATOR, order_number)
        return self.get_text_from_element(order_locator)

    @allure.step('Получаем количество завершенных заказов')
    def get_completed_orders_count(self, counter):
        count_locator = format_locator(OrderFeedPageLocators.COMPLETED_ORDERS_LOCATOR, counter)
        return self.get_text_from_element(count_locator)

    @allure.step('Получаем определенный заказ из списка "В работе"')
    def get_order_in_progress(self, order_number):
        order_number_without_zero = order_number[1:]
        order = '#' + self.get_text_from_element_with_waiting(OrderFeedPageLocators.IN_PROGRESS_ORDER_LOCATOR,
                                                              order_number_without_zero)
        return order
