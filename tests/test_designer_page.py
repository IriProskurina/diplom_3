from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common import TimeoutException
import allure
import pytest

from pages.login_page import LoginPage
from pages.designer_page import DesignerPage
from locators.designer_page_locators import DesignerPageLocators

class TestDesignerPage:

    @allure.title("Простой тест")
    def test_open_ingredient_modal_window(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_design_page()
        designer_page.open_ingredient_details()
        assert designer_page.get_ingredient_window_title() == "Детали ингредиента"

    @allure.title("Проверка закрытия модального окна ингредиента")
    def test_close_ingredient_modal_window(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_design_page()
        designer_page.open_ingredient_details()
        designer_page.close_ingredient_details()
        assert designer_page.check_visibility_of_modal_title()

    @allure.title("Счетчик ингредиента увеличивается, когда ингредиент добавлен в корзину")
    def test_ingredient_counter_increase_when_add_to_basket(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_design_page()
        counter_before = int(designer_page.get_ingredient_count())
        designer_page.drag_ingredient_to_basket(DesignerPageLocators.INGREDIENT_LOCATOR)
        counter_after = int(designer_page.get_ingredient_count())
        assert counter_after == counter_before + 1, \
            f"Счётчик не увеличился: до {counter_before}, после {counter_after}"

    @allure.title("Авторизированный пользователь может сделать заказ")
    def test_authorized_user_should_make_order(self, driver, user, login_page):
        designer_page = DesignerPage(driver)
        login_page.open_login_page()
        login_page.authorize_user(user.login, user.password)


    @allure.title("Клик по ингредиенту вызывает модальное окно")
    def test_click_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_design_page()
        designer_page.open_ingredient_details()
        assert designer_page.get_ingredient_window_title() == "Детали ингредиента"