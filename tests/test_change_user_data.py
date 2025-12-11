import allure
from data import *
from methods import *

@allure.feature('Тестирование редактирования данных пользователя')
class TestChangingUserData:

    @allure.title('Успешное редактирование данных пользователя')
    def test_changing_data_success(self, create_user_with_token):
        token = create_user_with_token
        response = UserMethods.changing_user_data(Data.MODIFIED_DATA, token)
        expected_response = {
            'success': True,
            'user': {
                'email': Data.MODIFIED_DATA['email'],
                'name': Data.MODIFIED_DATA['name']
            }
        }
        assert response.status_code == 200 and response.json() == expected_response

    @allure.title('Ошибка редактирования данных пользователя без авторизации')
    def test_changing_data_without_login_error(self, create_user_with_token):
        body = Data.MODIFIED_DATA
        token = ''
        response = UserMethods.changing_user_data(body, token)
        assert response.status_code == 401 and response.json() == response.json() == Data.unauthorized_error()
