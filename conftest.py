import pytest
import requests
from data import CREATE_COURIER_URL
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier_login():
    """Фикстура для регистрации нового курьера и возврата его данных для логина"""
    login, password, first_name = CourierMethods.register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    requests.post(CREATE_COURIER_URL, json=payload)
    return login, password, first_name

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
