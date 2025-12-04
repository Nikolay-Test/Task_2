import allure
from data import *
from methods import *

@allure.feature('Получение заказов конкретного пользователя')
class TestGetOrder:

    @allure.title('Успешное получение списка заказов конкретного пользователя')
    def test_get_order_success(self, create_user_with_token):
        response = OrderMethods.get_order(create_user_with_token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Ошибка получения списка заказов конкретного пользователя без авторизации')
    def test_get_order_without_registration_error(self):

        response = OrderMethods.get_order('')
        assert response.json() == Data.unauthorized_error() and response.status_code == 401
        