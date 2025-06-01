from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.designer_page_locators import DesignerPageLocators
from data import Links


class DesignerPage(BasePage):
    @allure.step('Открываем страницу конструктора')
    def open_design_page(self):
        self.open_url(Links.MAIN_LINK)

    @allure.step('Открываем детали ингредиента')
    def open_ingredient_details(self):
        self.click_to_element(DesignerPageLocators.INGREDIENT_LOCATOR)

    @allure.step('Закрываем детали ингредиента')
    def close_ingredient_details(self):
        self.click_to_element(DesignerPageLocators.MODAL_CLOSE_BUTTON_LOCATOR)

    @allure.step('Получаем тест заголовка')
    def get_title(self):
        return self.get_text_from_element(DesignerPageLocators.TITLE_LOCATOR)

    def get_ingredient_window_title(self):
        return self.get_text_from_element(DesignerPageLocators.MODAL_TITLE_LOCATOR)

    @allure.step('Проверяем видимость модального окна')
    def check_visibility_of_modal_title(self):
        modal_title_atr = self.get_attribute_of_element(DesignerPageLocators.MODAL_TITLE_LOCATOR, 'class')
        return 'opened' not in modal_title_atr

    @allure.step('Добавляем ингредиент в корзину')
    def drag_ingredient_to_basket(self, locator, delay=2, time=None):
        try:
            # Ждем и прокручиваем к ингредиенту
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Ждем и прокручиваемся к корзине (используем обновленный локатор)
            basket = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(DesignerPageLocators.BASKET_LOCATOR)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", basket)

            # Альтернативный способ перетаскивания (более надежный)
            ActionChains(self.driver).click_and_hold(element) \
                .move_to_element(basket) \
                .pause(1) \
                .release() \
                .perform()

            # Даем время для анимации
            time.sleep(delay)

        except Exception as e:
            # Делаем скриншот для отладки
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="drag_error",
                attachment_type=allure.attachment_type.PNG
            )
            # Логируем текущий DOM
            with open("drag_error_page.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise Exception(f"Ошибка при перетаскивании ингредиента: {str(e)}\nURL: {self.driver.current_url}")

    @allure.step('Получаем значение счетчика ингредиента')
    def get_ingredient_count(self):
        return self.get_text_from_element(DesignerPageLocators.COUNTER_INGREDIENT_LOCATOR)

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_to_make_order_button(self):
        self.click_to_element(DesignerPageLocators.MAKE_ORDER_BUTTON_LOCATOR)

    @allure.step('Оформляем заказ с бубликом и ингредиентом')
    def make_order_with_bun_and_ingredient(self):
        try:
            # Ждем доступность элементов и начинаем оформление заказа
            bun = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//path-to-bun"))
            )
            ingredient = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//path-to-ingredient"))
            )
            basket = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//path-to-basket"))
            )

            # Перетаскиваем ингредиенты в корзину
            ActionChains(self.driver) \
                .drag_and_drop(bun, basket) \
                .drag_and_drop(ingredient, basket) \
                .perform()

            # Завершаем оформление заказа
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//submit-button-path"))
            )
            submit_button.click()

        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="order_making_error",
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f"Ошибка при оформлении заказа: {str(e)}")

    @allure.step('Проверяем, что заказ подтвержден')
    def check_order_confirmation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(DesignerPageLocators.ORDER_CONFIRMATION_TEXT_LOCATOR)
        ).is_displayed()

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_to_make_order_button(self):
        self.click_to_element(DesignerPageLocators.MAKE_ORDER_BUTTON_LOCATOR)

    @allure.step('Делаем заказ с булкой и ингредиентом')
    def make_order_with_bun_and_ingredient(self):
        self.drag_ingredient_to_basket(DesignerPageLocators.BUN_LOCATOR)
        self.drag_ingredient_to_basket(DesignerPageLocators.INGREDIENT_LOCATOR)
        self.click_to_make_order_button()

    @allure.step('Проверяем, что заказ подтвержден')
    def check_order_confirmation(self):
        return self.find_element_with_waiting(DesignerPageLocators.ORDER_CONFIRMATION_TEXT_LOCATOR).is_displayed()

    def is_modal_visible(self):
        """Проверяет, видимо ли модальное окно"""
        try:
            element = self.driver.find_element(*DesignerPageLocators.MODAL_WINDOW_LOCATOR)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def is_basket_visible(self, локатор_корзины=None):
        return self.is_element_visible(локатор_корзины)

