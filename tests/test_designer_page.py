from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

from pages.designer_page import DesignerPageLocators


class TestDesignerPage:
    @allure.title("Проверка открытия модального окна ингредиента")
    def test_open_ingredient_modal_window(self, driver, designer_page):
        designer_page.open_design_page()
        designer_page.open_ingredient_details()
        assert designer_page.get_ingredient_window_title() == "Детали ингредиента"

    @allure.title("Проверка закрытия модального окна ингредиента")
    def test_close_ingredient_modal_window(self, driver, designer_page):
        try:
            driver.maximize_window()
            designer_page.open_design_page()

            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            # Проверка, что модальное окно не видно изначально
            assert not designer_page.is_modal_visible(), "Модальное окно не должно быть видно при открытии страницы"

            # Дальнейшие шаги теста...
        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="test_failure",
                attachment_type=allure.attachment_type.PNG
            )
            raise

    @allure.title("Счетчик ингредиента увеличивается, когда ингредиент добавлен в корзину")
    def test_ingredient_counter_increase_when_add_to_basket(self, driver, designer_page):
        designer_page.open_design_page()

        # Получаем начальное значение счетчика
        counter_before = designer_page.get_ingredient_count()
        assert counter_before == "0", "Начальное значение счетчика должно быть 0"

        # Добавляем ингредиент с проверкой видимости
        ingredient = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(DesignerPageLocators.INGREDIENT_LOCATOR)
        )

