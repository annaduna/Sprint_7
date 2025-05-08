import allure
from method.order_method import OrderMethods

class TestOrdersList:
    @allure.title('тест на получение списка заказов')
    def test_get_orders_list(self):
        response = OrderMethods.get_orders_list()
        assert response.status_code == 200 and "orders" in response.json()