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