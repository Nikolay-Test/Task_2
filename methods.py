import requests
from urls import *
import allure

class AuthMethods:

    @staticmethod
    @allure.step("Получить токены авторизации")
    def get_tokens(body):
        response = requests.post(LOGIN, json=body)
        return response.json()['accessToken']


class OrderMethods:

    @staticmethod
    @allure.step("Создать новый заказ")
    def create_order(body, token):
        return requests.post(ORDER, json=body, headers={'Authorization': token})

    @staticmethod
    @allure.step("Получить информацию о заказе")
    def get_order(token):
        return requests.get(ORDER, headers={'Authorization': token})
    

class UserMethods:

    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def registration_user(body):
        return requests.post(REGISTRY, json=body)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(body):
        return requests.post(LOGIN, json=body)

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def changing_user_data(body, token):
        return requests.patch(USER, json=body, headers={'Authorization': token})

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(DELETE, headers={'Authorization': token})
    