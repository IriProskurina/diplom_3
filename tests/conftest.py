import pytest
from selenium import webdriver
from helpers import register_user, delete_user
from pages.login_page import LoginPage
from pages.designer_page import DesignerPage
from pages.header_page import HeaderPage
from pages.account_page import AccountPage
from pages.recovery_page import RecoveryPage
from pages.order_feed_page import OrderFeedPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def user():
    u = register_user()
    yield u               # u -- объект User
    delete_user(u.access_token)

@pytest.fixture()
def designer_page(driver):
    return DesignerPage(driver)

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def recovery_page(driver):
    return RecoveryPage(driver)

@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)