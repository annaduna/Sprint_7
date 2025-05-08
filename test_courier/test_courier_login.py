import allure
import pytest
from generators import generate_courier
from method.courier_method import CourierMethod


@allure.description("Тест проверяет успешную авторизацию курьера")
def test_courier_login_success(courier_cleanup):
        courier_data = generate_courier()
        create_response = CourierMethod.create_courier(courier_data)
        assert create_response.status_code == 201, "Курьер не создан"

        courier_id = CourierMethod.get_courier_id(courier_data)
        courier_cleanup(courier_id)
        login_response = CourierMethod.post_login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert login_response.status_code == 200
        assert "id" in login_response.json()


@allure.description("Тест проверяет авторизацию без поля 'login'")
def test_courier_login_missing_login(courier_cleanup):
    courier_data = generate_courier()
    create_response = CourierMethod.create_courier(courier_data)
    assert create_response.status_code == 201, "Курьер не создан"

    courier_id = CourierMethod.get_courier_id(courier_data)
    courier_cleanup(courier_id)

    courier_data.pop("login")
    login_response = CourierMethod.post_login_courier(courier_data)
    assert login_response.status_code == 400
    assert login_response.json().get("message") == "Недостаточно данных для входа"


@allure.description("Тест проверяет авторизацию без поля 'password'")
def test_courier_login_missing_password(courier_cleanup):
    courier_data = generate_courier()
    create_response = CourierMethod.create_courier(courier_data)
    assert create_response.status_code == 201, "Курьер не создан"

    courier_id = CourierMethod.get_courier_id(courier_data)
    courier_cleanup(courier_id)

    courier_data.pop("password")

    login_response = CourierMethod.post_login_courier(courier_data)
    assert login_response.status_code == 400
    assert login_response.json().get("message") == "Недостаточно данных для входа"


@allure.description("Тест проверяет авторизацию с неверным логином и паролем")
def test_courier_login_invalid_credentials(courier_cleanup):
    login_data = {
        "login": "ghmghmg",
        "password": "5474635"
    }
    login_response = CourierMethod.post_login_courier(login_data)
    assert login_response.status_code == 404
    assert login_response.json().get("message") == "Учетная запись не найдена"




