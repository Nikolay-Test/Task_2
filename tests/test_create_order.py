import allure
import pytest
from data import *
from methods import *
from urls import *

@allure.feature('Тестирование создания заказа')
class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией пользователя')
    def test_create_order_success(self, create_user_with_token):
        response = OrderMethods.create_order(Data.ORDER, create_user_with_token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание заказа без авторизации пользователя')
    def test_create_order_without_registration(self):
        response = OrderMethods.create_order(Data.ORDER, None)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Успешное создание заказа с ингредиентами')
    def test_create_order_with_ingredients_success(self, create_user_with_token):
        response = OrderMethods.create_order(Data.ORDER, create_user_with_token)
        response_data = response.json()
        
        # Проверяем основную структуру ответа
        assert response.status_code == 200
        assert response_data.get('success') is True
        assert 'order' in response_data
        assert 'name' in response_data['order']
        assert '_id' in response_data['order']  # или 'number', в зависимости от API
        
        # Проверяем наличие ингредиентов
        assert 'ingredients' in response_data['order']
        assert len(response_data['order']['ingredients']) > 0

    @allure.title('Ошибка создания заказа с пустыми ингредиентами')
    def test_order_with_empty_ingredients_error(self, create_user_with_token):
        body, status_code, success, response_text = Data.INGREDIENTS[0]
        response = OrderMethods.create_order(body, create_user_with_token)
        assert response.status_code == status_code
        assert response.json() == {'success': success, 'message': response_text}

    @allure.title('Ошибка создания заказа с некорректными идентификаторами ингредиентов')
    def test_order_with_invalid_ingredient_ids_error(self, create_user_with_token):
        body, status_code, success, response_text = Data.INGREDIENTS[1]
        response = OrderMethods.create_order(body, create_user_with_token)
        assert response.status_code == status_code
        # Проверяем, что в ответе есть текст ошибки (но не проверяем точный формат)
        assert response_text in response.text
        