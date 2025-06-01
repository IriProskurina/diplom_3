import pytest
from selenium import webdriver
from helpers import register_user, delete_user
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage
from pages.header_page import HeaderPage
from pages.designer_page import DesignerPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def user():
    user = register_user()
    yield user
    delete_user(user.access_token)


@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture()
def recovery_page(driver):
    recovery_page = RecoveryPage(driver)
    return recovery_page


@pytest.fixture()
def header_page(driver):
    header_page = HeaderPage(driver)
    return header_page


@pytest.fixture()
def designer_page(driver):
    designer_page = DesignerPage(driver)
    return designer_page


@pytest.fixture()
def order_feed_page(driver):
    order_feed_page = OrderFeedPage(driver)
    return order_feed_page


@pytest.fixture()
def account_page(driver):
    account_page = AccountPage(driver)
    return account_page
