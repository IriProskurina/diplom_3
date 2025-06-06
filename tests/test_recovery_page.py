import pytest
import allure
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage

class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_transition_to_recovery_page_from_login_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page.open_login_page()
        login_page.click_to_recovery_button()
        assert recovery_page.get_title() == "Восстановление пароля"

    @allure.title('При вводе почты и нажатии на кнопку "Восстановить" отображается форма изменения пароля')
    def test_add_email_and_click_to_recovery_button(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_recovery_page()
        recovery_page.fill_email()
        recovery_page.click_to_recovery_button()
        assert recovery_page.get_key_placeholder_text() == "Введите код из письма"

    @allure.title('Поле пароль подсвечивается при клике по кнопке показать/скрыть пароль')
    def test_check_password_highlight_on_click(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_recovery_page()
        recovery_page.click_to_recovery_button()
        recovery_page.click_to_show_hide_password_icon()
        assert recovery_page.check_highlight_password_field()
