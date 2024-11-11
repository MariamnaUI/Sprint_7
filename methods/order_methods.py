import requests
from data import ORDER_DATA, ORDER_URL


class OrderMethods:
    @staticmethod
    def create_order(**kwargs):
        payload = ORDER_DATA.copy()
        payload.update(kwargs)
        timeout = 3
        response = requests.post(ORDER_URL, json=payload, timeout=timeout)
        return response
