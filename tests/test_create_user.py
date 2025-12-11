import allure
import pytest
from data import *
from methods import *
from urls import *

@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    def test_create_user_success(self, create_and_delete_user):
        response = UserMethods.registration_user(create_and_delete_user)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Ошибка при создании двух одинаковых пользователей')
    def test_create_two_identical_users_error(self, create_and_delete_user):

        UserMethods.registration_user(create_and_delete_user)
        response = UserMethods.registration_user(create_and_delete_user)
        assert response.status_code == 403 and response.json() == Data.user_exists_error()

    @allure.title('Невозможность создания пользователя с пропущенным полем')
    @pytest.mark.parametrize('body, status_code, success, response_text', Data.JSON_WITH_EMPTY_FIELD)
    def test_create_user_with_missing_field_error(self, body, status_code, success, response_text):
        response = UserMethods.registration_user(body)
        expected_response = {
            'success': success,
            'message': response_text
        }
        assert response.status_code == status_code and response.json() == expected_response
        