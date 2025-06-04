import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.designer_page_locators import DesignerPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL: {url}")
    def open_url(self, url):
        self.driver.get(url)
        self.loader_waiting()

    @allure.step("Кликнуть по элементу с локатором: {locator}")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        self.loader_waiting()

    @allure.step("Поиск элемента с ожиданием по локатору: {locator}")
    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Получить текст из элемента с локатором: {locator}")
    def get_text_from_element(self, locator):
        return self.find_element_with_waiting(locator).text

    @allure.step("Ввести текст '{text}' в элемент с локатором: {locator}")
    def add_text_to_element(self, locator, text):
        self.find_element_with_waiting(locator).send_keys(text)

    @allure.step("Получить значение атрибута '{attribute}' у элемента с локатором: {locator}")
    def get_attribute_of_element(self, locator, attribute):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step("Получить текущий URL")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Проверить видимость элемента с локатором: {locator}")
    def check_visibility_of_element(self, locator):
        return self.find_element_with_waiting(locator).is_displayed()

    @allure.step("Прокрутить к элементу с локатором: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения лоадера")
    def loader_waiting(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located(locator=DesignerPageLocators.LOADER_LOCATOR)
            )
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located(locator=DesignerPageLocators.LOADER_LOCATOR)
            )
        except TimeoutException:
            pass

    @allure.step("Перетащить элемент c локатора {start_locator} на элемент с локатором {finish_locator}")
    def drag_and_drop_element(self, start_locator, finish_locator):
        draggable = self.find_element_with_waiting(start_locator)
        droppable = self.find_element_with_waiting(finish_locator)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    @allure.step("Дождаться появления текста '{order_number}' в элементе с локатором: {locator}")
    def get_text_from_element_with_waiting(self, locator, order_number):
        self.find_element_with_waiting(locator)
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, order_number))
        return order_number



