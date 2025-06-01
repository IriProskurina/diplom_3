import allure


class TestHeaderPage:
    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    def test_transition_by_order_feed_button(self, driver, header_page, designer_page, order_feed_page):
        designer_page.open_design_page()
        header_page.click_to_order_feed_button()
        assert order_feed_page.get_title() == "Лента заказов"

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_transition_by_designer_button(self, driver, header_page, designer_page):
        designer_page.open_design_page()
        header_page.click_to_order_feed_button()
        header_page.click_to_designer_button()
        assert designer_page.get_title() == "Соберите бургер"
