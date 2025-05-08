import requests
import json
import allure
from curl import url

class OrderMethods:
    @staticmethod
    @allure.step('Создаем новый заказ')
    def post_create_order(order_data):
        return requests.post(url. POST_CREATE_ORDERS_URL, data=json.dumps(order_data))

    @staticmethod
    @allure.step('Получаем список заказов')
    def get_orders_list():
        return requests.get(url.GET_LIST_ORDERS)