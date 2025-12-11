import allure
from methods import *
from data import *

@allure.feature('Тестирование логина пользователя')
class TestLogin:

    @allure.title('Успешная авторизация')
    def test_successful_login(self, create_and_delete_user):
        UserMethods.registration_user(create_and_delete_user)
        response = UserMethods.login_user(create_and_delete_user)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Ошибка авторизации при некорректном логине')
    def test_auth_with_incorrect_login_error(self, create_and_delete_user):
        UserMethods.registration_user(create_and_delete_user)
        response = UserMethods.login_user(Data.invalid_login_data(create_and_delete_user))
        assert response.status_code == 401 and response.json() == Data.invalid_credentials_error()

    @allure.title('Ошибка авторизации при некорректном пароле')
    def test_auth_with_incorrect_password_error(self, create_and_delete_user):
        UserMethods.registration_user(create_and_delete_user)
        invalid_password_data = {
            'email': create_and_delete_user['email'],
            'password': 'invalidpassword'
        }
        response = UserMethods.login_user(invalid_password_data)
        assert response.status_code == 401 and response.json() == Data.invalid_credentials_error()
        