from helpers import fake_data
from datetime import datetime


class Data:

    @staticmethod
    def user_body():
        email, password, name = fake_data()
        return {
            'email': email,
            'password': password,
            'name': name
        }
    

    @staticmethod
    def user_exists_error():
        return {
            'success': False,
            'message': 'User already exists'
        }


    @staticmethod
    def invalid_credentials_error():
        return {
            'success': False,
            'message': 'email or password are incorrect'
        }

    @staticmethod
    def invalid_login_data(valid_user):
        return {
            'email': 'wrong@example.com',
            'password': valid_user['password']
        }

    @staticmethod
    def unauthorized_error():
        return {
            'success': False,
            'message': 'You should be authorised'
        }

    JSON_WITH_EMPTY_FIELD = (
        ({
            'email': '',
            'password': user_body()['password'],
            'name': user_body()['name']
        }, 403, False, 'Email, password and name are required fields'),
        ({
            'email': user_body()['email'],
            'password': '',
            'name': user_body()['name']
        }, 403, False, 'Email, password and name are required fields'),
        ({
            'email': user_body()['email'],
            'password': user_body()['password'],
            'name': ''
        }, 403, False, 'Email, password and name are required fields')
    )

    ORDER =  {
        'ingredients': [
            '61c0c5a71d1f82001bdaaa73',
            '61c0c5a71d1f82001bdaaa6c', 
            '61c0c5a71d1f82001bdaaa79' 
        ]
    }

    INGREDIENTS = (
        ({
            'ingredients': ''
        }, 400, False, 'Ingredient ids must be provided'),
        ({
            'ingredients': ['1234', 'qwerty', '!@#$%']
        }, 500, 'Error', 'Internal Server Error')
    )

    MODIFIED_DATA = {
        'email': f"updated_{datetime.now().strftime('%Y%m%d')}@example.com", 
        'password': "NewPass123!",
        'name': 'Updated User'
    }
    