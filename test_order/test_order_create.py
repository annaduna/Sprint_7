import allure
import pytest
from data import DataForOrder
from method.order_method import OrderMethods


class TestCreateOrder:
    @allure.title('Проверяем создание заказа с разными цветами и что тело ответа содержит track')
    @pytest.mark.parametrize('color', (['BLACK'], ['GREY'], ['BLACK', 'GREY'], []))
    def test_create_order_with_different_color(self, color):
        order_data = DataForOrder.CREATE_ORDERS
        order_data["color"] = color
        response = OrderMethods.post_create_order(order_data)
        assert response.status_code == 201 and 'track' in response.json()