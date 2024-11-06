import allure
import pytest
from data import LOGIN_COURIER_URL, COURIER_NULL_DATA_SETS


@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Проверка, на успешную авторизацию курьера")
    def test_login_courier_success(self, request_with_timeout, courier_login):
        login, password, _ = courier_login
        payload = {
            "login": login,
            "password": password
        }
        response = request_with_timeout('POST', LOGIN_COURIER_URL, json=payload)
        response_data = response.json()
        assert response.status_code == 200 and "id" in response_data and response_data["id"] > 0

    @pytest.mark.parametrize(
        "payload, expected_status_code, response_text", [
            ({"login": "somelogin"}, 400, '{"code":400,"message":"Недостаточно данных для входа"}'),
            ({"password": "somepassword"}, 400, '{"code":400,"message":"Недостаточно данных для входа"}'),
            ({}, 400, '{"code":400,"message":"Недостаточно данных для входа"}')
        ]
    )
    @allure.title("Проверка, что при отсутствии обязательных полей, курьер не создаётся")
    def test_login_courier_without_required_fields(self, request_with_timeout, payload, expected_status_code, response_text, courier_login):
        login, password, _ = courier_login
        response = request_with_timeout('POST', LOGIN_COURIER_URL, json=payload)
        assert response.status_code == expected_status_code and response.text == response_text

    @pytest.mark.parametrize(
        "login, password, expected_status_code, response_text", [
            ("falselogin", "falsepassword", 404, '{"code":404,"message":"Учетная запись не найдена"}'),
            ("rightlogin", "falsepassword", 404, '{"code":404,"message":"Учетная запись не найдена"}'),
            ("falselogin", "rightpassword", 404, '{"code":404,"message":"Учетная запись не найдена"}'),
            ("", "", 400, '{"code":400,"message":"Недостаточно данных для входа"}')
        ]
    )
    @allure.title("Проверка наличия ошибки при неправильном логине или пароле")
    def test_login_courier_false_fields(self, request_with_timeout, login, password, expected_status_code, response_text):
        payload = {
            "login": login,
            "password": password
        }
        response = request_with_timeout('POST', LOGIN_COURIER_URL, json=payload)
        assert response.status_code == expected_status_code and response.text == response_text

    @allure.title("Проверка наличия ошибки при попытке логина несуществующего курьера")
    def test_login_null_courier(self, request_with_timeout):
        payload = COURIER_NULL_DATA_SETS[0]
        response = request_with_timeout('POST', LOGIN_COURIER_URL, json=payload)
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Учетная запись не найдена"}'
