import allure
import requests
from curl import url

class CourierMethod:
    @staticmethod
    @allure.description("Функция для создания курьера")
    def create_courier(courier_data):
        return requests.post(url.CREATE_COURIER_URL, json=courier_data)

    @staticmethod
    @allure.description("Метод для получения ID курьера")
    def get_courier_id(courier_data):
        courier_data2 = {"login": courier_data["login"], "password": courier_data["password"]}
        login_response = requests.post(url.POST_COURIER_LOGIN, json=courier_data2)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        courier_id = login_response_json.get("id")  #
        assert courier_id is not None, "Ошибка: ID курьера не найден!"
        return courier_id

    @staticmethod
    @allure.step('Метод Авторизации курьера')
    def post_login_courier(login_data):
        return requests.post(url.POST_COURIER_LOGIN, json=login_data)