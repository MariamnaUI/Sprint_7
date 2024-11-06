import allure
import pytest
from methods.order_methods import OrderMethods


@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize(
        "color, expected_status_code, response_text", [
            (["BLACK"], 201, "track"),
            (["GREY"], 201, "track"),
            (["BLACK", "GREY"], 201, "track"),
            ([], 201, "track")
        ])
    @allure.title("Проверка создания заказа с различными цветами")
    def test_create_order_with_colors(self, color, expected_status_code, response_text):
        order_methods = OrderMethods()
        response = order_methods.create_order(color=color)
        assert response.status_code == expected_status_code and "track" in response_text
