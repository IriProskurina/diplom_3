import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from helpers import make_order
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from pages.account_page import AccountPage

class TestOrderFeedPage:
    @allure.title('По клику на заказ, открывается всплывающее окно с деталями')
    def test_open_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        order_number_from_feed = order_feed_page.get_order_number_from_feed()
        order_feed_page.open_order_details()
        order_number_from_details = order_feed_page.get_order_number_from_order_details()
        assert order_number_from_feed == order_number_from_details

    @allure.title('Заказы пользователя из истории отображаются на странице "Лента заказов"')
    def test_user_order_displayed_in_order_feed(self, driver, user):
        login_page = LoginPage(driver)
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

    @allure.title('Заказы пользователя из истории отображаются на странице "Лента заказов"')
    def test_user_order_displayed_in_order_feed(self, driver, user):
        login_page = LoginPage(driver)
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        make_order(user.access_token)
        login_page.open_login_page()
        login_page.authorize_user(login=user.login, password=user.password)
        header_page.click_to_account_button()
        account_page.click_to_order_history_button()
        order_number_from_account = account_page.get_order_number()
        header_page.click_to_order_feed_button()
        order_feed_page.scroll_to_order(order_number_from_account)
        order_number_from_order_feed = order_feed_page.get_specific_order_from_order_feed(order_number_from_account)
        assert order_number_from_order_feed == order_number_from_account

    @pytest.mark.parametrize('counter', ['Выполнено за все время:', 'Выполнено за сегодня:'],
                             ids=['выполнено за все время', 'выполнено за сегодня'])
    @allure.title('Счетчик заказов увеличивается при оформлении заказа')
    def test_completed_orders_increase_when_user_make_order(self, driver, user, counter):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        orders_count_before = order_feed_page.get_completed_orders_count(counter)
        make_order(user.access_token)

        # Ждем, пока счетчик увеличится
        WebDriverWait(driver, 30).until(
            lambda x: order_feed_page.get_completed_orders_count(counter) > orders_count_before,
            message=f"Счетчик не обновился: {orders_count_before} → {order_feed_page.get_completed_orders_count(counter)}"
        )
        orders_count_after = order_feed_page.get_completed_orders_count(counter)
        assert orders_count_before < orders_count_after

    @allure.title('Оформленный заказ отображается в ленте в процессе')
    def test_order_displayed_in_in_progress_feed_when_user_make_order(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        order = make_order(user.access_token)
        assert order_feed_page.get_order_in_progress(order) == order

