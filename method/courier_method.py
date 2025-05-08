import allure
import requests
from curl import url

# class CourierMethods:
@allure.description("Функция для создания курьера")
def create_courier(courier_data):
    return requests.post(url.CREATE_COURIER_URL, json=courier_data)

def get_courier_id(courier_data):
    courier_data2 = {"login": courier_data["login"], "password": courier_data["password"]}
    login_response = requests.post(url.POST_COURIER_LOGIN, json=courier_data2)
    assert login_response.status_code == 200  # Проверяем успешный вход
    login_response_json = login_response.json()
    courier_id = login_response_json.get("id")  # Получаем ID курьера
    assert courier_id is not None, "Ошибка: ID курьера не найден!"
    return courier_id