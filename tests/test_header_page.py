import allure
from pages.header_page import HeaderPage
from pages.designer_page import DesignerPage
from pages.order_feed_page import OrderFeedPage


class TestHeaderPage:
    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    def test_transition_by_order_feed_button(self, driver):
        designer_page = DesignerPage(driver)
        header_page = HeaderPage(driver)
        order_feed_page = OrderFeedPage(driver)

        designer_page.open_design_page()
        header_page.click_to_order_feed_button()
        assert order_feed_page.get_title() == "Лента заказов"

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_transition_by_designer_button(self, driver):
        designer_page = DesignerPage(driver)
        header_page = HeaderPage(driver)

        designer_page.open_design_page()
        header_page.click_to_order_feed_button()
        header_page.click_to_designer_button()
        assert designer_page.get_title() == "Соберите бургер"
