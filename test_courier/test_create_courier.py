import allure
from method.courier_method import CourierMethod
from data import DataForCourier
from generators import generate_courier

@allure.description("Тест проверяет, что курьер успешно создаётся и возвращает правильный код ответа и тело ответа. Все обязательные поля переданы. ")
def test_create_courier_success(courier_cleanup):
    response = CourierMethod.create_courier(DataForCourier.CREATE_COURIER)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json.get("ok") is True

    courier_id = CourierMethod.get_courier_id(DataForCourier.CREATE_COURIER)
    courier_cleanup(courier_id)

@allure.description("Тест проверяет, что нельзя создать двух курьеров с одинаковыми данными. Также проверка на то что если создать пользователя с логином, который уже есть, возвращается ошибка.")
def test_create_duplicate_courier(courier_cleanup):

    response = CourierMethod.create_courier(DataForCourier.CREATE_COURIER)
    assert response.status_code == 201
    courier_id = CourierMethod.get_courier_id(DataForCourier.CREATE_COURIER)

    courier_cleanup(courier_id)

    second_response = CourierMethod.create_courier(DataForCourier.CREATE_COURIER)
    assert second_response.status_code == 409

    second_create_courier_text = second_response.json()
    assert second_create_courier_text.get("message") == "Этот логин уже используется. Попробуйте другой."

@allure.description("Тест проверяет, что запрос без обязательного поля возвращает ошибку 400.")
def test_create_courier_without_login():
    courier_data = generate_courier()
    courier_data.pop("login")
    response = CourierMethod.create_courier(courier_data)
    assert response.status_code == 400
    response_json = response.json()
    assert response_json.get("message") == "Недостаточно данных для создания учетной записи"






