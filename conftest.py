import pytest
import requests
from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier_login():
    """Фикстура для регистрации нового курьера, возврата его данных для логина и удаления после теста"""
    # Создание курьера
    login, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    create_response = requests.post(CREATE_COURIER_URL, json=payload)
    assert create_response.status_code == 201

    # Получение ID курьера
    login_payload = {
        "login": login,
        "password": password
    }
    login_response = requests.post(LOGIN_COURIER_URL, json=login_payload)
    courier_id = login_response.json().get("id")

    yield login, password, first_name

    # Удаление курьера после завершения теста
    if courier_id:
        delete_response = requests.delete(f"{DELETE_COURIER_URL}/{courier_id}")
        if delete_response.status_code != 200:
            print('"ok": true')
        else:
            print('"code": 404,"message": "Курьера с таким id нет."')

@pytest.fixture
def request_with_timeout():
    """Фикстура для таймаутов"""
    def _request(method, url, **kwargs):
        timeout = 3
        try:
            response = requests.request(method, url, timeout=timeout, **kwargs)
            return response
        except requests.exceptions.Timeout:
            pytest.fail("Таймаут при запросе")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Ошибка запроса: {e}")
    return _request
