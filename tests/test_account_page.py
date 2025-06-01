import allure


class TestAccountPage:
    @allure.title('Переход в личный кабинет по кнопке "Личный кабинет"')
    def test_transition_from_account_page(self, driver, user, login_page, header_page, account_page):
        login_page.open_login_page()
        login_page.authorize_user(login=user.login, password=user.password)
        header_page.click_to_account_button()
        assert account_page.get_name() == user.name

    @allure.title('Переход на страницу истории заказов')
    def test_transition_to_order_history(self, driver, user, login_page, header_page, account_page):
        login_page.open_login_page()
        login_page.authorize_user(login=user.login, password=user.password)
        header_page.click_to_account_button()
        account_page.click_to_order_history_button()
        assert account_page.check_active_history_button() and account_page.check_order_history_url()

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_account(self, driver, user, login_page, header_page, account_page):
        login_page.open_login_page()
        login_page.authorize_user(login=user.login, password=user.password)
        header_page.click_to_account_button()
        account_page.click_to_exit_button()
        assert login_page.get_title() == "Вход"
