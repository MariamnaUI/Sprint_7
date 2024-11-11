import allure
import requests
from data import ORDER_URL, COURIER_ID


@allure.feature("Список заказов")
class TestGetOrders:
    @allure.title("Проверка, что в тело ответа возвращается список заказов")
    def test_get_orders_list(self):
        response = requests.get(f"{ORDER_URL}?courierId={COURIER_ID}")
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
        response_data = response.json()

        assert 'orders' in response_data and isinstance(response_data['orders'], list)
