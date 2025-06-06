import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import Links


class LoginPage(BasePage):
    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        self.open_url(Links.LOGIN_PAGE_LINK)

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_to_recovery_button(self):
        self.click_to_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON_LOCATOR)

    @allure.step('Заполняем поля e-mail и пароль')
    def fill_email_and_password(self, email, password):
        self.add_text_to_element(LoginPageLocators.EMAIL_LOCATOR, email)
        self.add_text_to_element(LoginPageLocators.PASSWORD_LOCATOR, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_to_enter_button(self):
        self.click_to_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Авторизуемся')
    def authorize_user(self, login, password):
        self.fill_email_and_password(login, password)
        self.click_to_enter_button()

    @allure.step('Получаем заголовок: "Вход"')
    def get_title(self):
        return self.get_text_from_element(LoginPageLocators.HEADING_TEXT_LOCATOR)
