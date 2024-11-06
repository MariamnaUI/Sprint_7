BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
CREATE_COURIER_URL = f'{BASE_URL}/courier'
LOGIN_COURIER_URL = f'{BASE_URL}/courier/login'
ORDER_URL = f'{BASE_URL}/orders'

COURIER_NULL_DATA_SETS = [{"login": "mariahhhvvvfgb111", "password": "1234", "firstName": "Мари"}]

ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": None
}

COURIER_ID = 420528
