import random
import secrets
import string
import requests
from data import Links, Endpoints


class Error(Exception):
    pass


class User:
    def __init__(self, login, password):
        self.name = "generate_random_string"
        self.login = login
        self.password = password
        self.access_token = None


def login_generator():
    name = "generate_random_string"
    domain = "@email.com"
    login = name + str(random.randint(100, 999)) + domain
    return login


def password_generator():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def register_user():
    login = login_generator()
    password = password_generator()
    user = User(login, password)

    payload = {
        "email": user.login,
        "password": user.password,
        "name": user.name
    }

    response = requests.post(Links.MAIN_LINK + Endpoints.REGISTER_ENDPOINT, data=payload)
    if response.status_code == 200:
        user.access_token = response.json()["accessToken"]
        return user
    else:
        raise Error("Пользователь не зарегистрирован")


def delete_user(token):
    response = requests.delete(Links.MAIN_LINK + Endpoints.USER_ENDPOINT, headers={'Authorization': token})
    if response.status_code != 202:
        raise Error("Пользователь не удален")


def create_burger():
    burger = []
    burger_types = ['bun', 'main', 'sauce']
    response = requests.get(Links.MAIN_LINK + Endpoints.INGREDIENTS_ENDPOINT)
    if response.status_code == 200:
        for types in burger_types:
            for ingredients in response.json()['data']:
                if ingredients['type'] == types:
                    burger.append(ingredients['_id'])
                    break
    else:
        raise Error("response.status_code != 200")
    return burger


def make_order(token):
    burger_ingredients = create_burger()
    payload = {"ingredients": burger_ingredients}
    response = requests.post(Links.MAIN_LINK + Endpoints.ORDER_ENDPOINT, headers={'Authorization': token}, data=payload)
    order_number = '#0' + str(response.json()['order']['number'])
    return order_number


def format_locator(locator_a, num):
    method, locator = locator_a
    locator = locator.format(num)
    return method, locator
