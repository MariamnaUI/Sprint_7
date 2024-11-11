import allure
import pytest
from data import CREATE_COURIER_URL
from methods.courier_methods import CourierMethods


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера")
    def test_create_courier_success(self, request_with_timeout):
        login, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = request_with_timeout('POST', CREATE_COURIER_URL, json=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title("Проверка, что нельзя создать курьера с существующим логином")
    def test_create_duplicate_courier(self, request_with_timeout, courier_login):
        login, password, first_name = courier_login
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = request_with_timeout('POST', CREATE_COURIER_URL, data=payload)
        assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @pytest.mark.parametrize(
        "missing_field, expected_status_code, response_text", [
            ("login", 400, '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'),
            ("password", 400, '{"code":400,"message":"Недостаточно данных для создания учетной записи"}')
        ]
    )
    @allure.title("Проверка, что при отсутствии обязательных полей, курьер не создаётся")
    def test_create_courier_without_required_fields(self, request_with_timeout, missing_field, expected_status_code, response_text, courier_login):
        login, password, first_name = courier_login
        payload = {
            "login": login if missing_field != "login" else None,
            "password": password if missing_field != "password" else None,
            "firstName": first_name
        }
        payload = {key: value for key, value in payload.items() if value is not None}
        response = request_with_timeout('POST', CREATE_COURIER_URL, json=payload)
        assert response.status_code == expected_status_code and response.text == response_text
