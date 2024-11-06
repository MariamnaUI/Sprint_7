# Sprint_7 

## Описание структуры проекта 

### Файлы 

conftest.py - файл с текстурами  
data.py - данные, используемые в тестах   

**tests - директория с тестами** 

* test_create_courier.py - тесты для создания курьера  
* test_login_courier.py - тесты для логина курьера  
* test_create_order.py - тесты для создания заказа 
* test_get_orders.py - тесты для получения списка заказов 

**methods - директория с базовыми методами**

* courier_methods.py - методы для работы с общими элементами проекта
* order_methods.py - методы для главной страницы

### Краткое описание тестов 

test_create_courier_success - тест на успешное создание курьера  
test_create_duplicate_courier - тест, что нельзя создать курьера с существующим логином  
test_create_courier_without_required_fields - тест, что при отсутствии обязательных полей, курьер не создаётся  
test_login_courier_success - тест на успешную авторизацию курьера  
test_login_courier_without_required_fields - тест, что при отсутствии обязательных полей, курьер не создаётся  
test_login_courier_false_fields - тест, что будет ошибка при неправильном логине или пароле  
test_login_null_courier - тест, что будет ошибка при попытке логина несуществующего курьера  
test_create_order_with_colors - тест на проверку создания заказа с различными цветами  
test_get_orders_list - тест, что в тело ответа возвращается список заказов  
