import allure

from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators
from data import Links


class RecoveryPage(BasePage):
    @allure.step('Открываем страницу восстановдения пароля')
    def open_recovery_page(self):
        self.open_url(Links.RECOVERY_PAGE_LINK)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_to_recovery_button(self):
        self.click_to_element(RecoveryPageLocators.RECOVERY_BUTTON_LOCATOR)

    @allure.step('Заполняем e-mail')
    def fill_email(self):
        self.add_text_to_element(RecoveryPageLocators.EMAIL_LOCATOR, 'test@test.com')

    @allure.step('Получаем текст заголовка: "Восстановление пароля"')
    def get_title(self):
        return self.get_text_from_element(RecoveryPageLocators.TITLE_LOCATOR)

    @allure.step('Получаем текст плейсхолдера поля Код')
    def get_key_placeholder_text(self):
        return self.get_text_from_element(RecoveryPageLocators.KEY_PLACEHOLDER_LOCATOR)

    @allure.step('Нажимаем на иконку показа/скрытия пароля')
    def click_to_show_hide_password_icon(self):
        self.click_to_element(RecoveryPageLocators.SHOW_HIDE_PASSWORD_ICON_LOCATOR)

    @allure.step('Проверяем, что поле ввода пароля подсвечивается ')
    def check_highlight_password_field(self):
        return ('input_status_active' in
                self.get_attribute_of_element(RecoveryPageLocators.HIGHLIGHT_ACTIVE_PASSWORD_LOCATOR, 'class'))
