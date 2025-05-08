import json
import allure
from create_couriers_methods import create_courier, get_courier_id
from data import url, DataForCourier
from generators import generate_courier


@allure.description("Тест проверяет, что курьер успешно создаётся и возвращает правильный код ответа и тело ответа. Все обязательные поля переданы. ")
def test_create_courier_success(courier_cleanup): # Фикстуры в pytest - это специальные функции, которые должны быть явно запрошены тестом через параметры /Когда pytest видит параметр с именем существующей фикстуры, он автоматически вызывает эту фикстуру и передаёт её результат в тест
    response = create_courier(DataForCourier.CREATE_COURIER) #json=courier_data в самой функции криейт курьер уже есть сериализация
    assert response.status_code == 201
    response_json = response.json() #json.loads(response.text) (десериализация)
    assert response_json.get("ok") is True

    courier_id = get_courier_id(DataForCourier.CREATE_COURIER)
    courier_cleanup(courier_id)

@allure.description("Тест проверяет, что нельзя создать двух курьеров с одинаковыми данными. Также проверка на то что если создать пользователя с логином, который уже есть, возвращается ошибка.")
def test_create_duplicate_courier(courier_cleanup):

    response = create_courier(DataForCourier.CREATE_COURIER)
    assert response.status_code == 201  # Проверяем успешное создание
    courier_id = get_courier_id(DataForCourier.CREATE_COURIER)

    # Теперь register_id содержит функцию register_courier_for_cleanup/ вызывая курьер клин-ап она возвращает нам функцию, не саму фикстуру, достигая елд.
    courier_cleanup(courier_id)  # Это вызов той самой функции, которую мы получили и сохранили в register_id. Функция добавляет переданный courier_id в список courier_ids внутри фикстуры
    #После теста фикстура проходит блок после yield и удаляет всех курьеров из списка.
    second_response = create_courier(DataForCourier.CREATE_COURIER)
    assert second_response.status_code == 409  # Проверяем успешное создание

    second_create_courier_text = second_response.json()
    assert second_create_courier_text.get("message") == "Этот логин уже используется. Попробуйте другой."

@allure.description("Тест проверяет, что запрос без обязательного поля возвращает ошибку 400.")
def test_create_courier_without_login():
    courier_data = generate_courier()  # Генерируем данные
    courier_data.pop("login")  # Удаляем логин перед отправкой
    response = create_courier(courier_data)  # Отправляем запрос
    assert response.status_code == 400  # Проверяем, что сервер отклонил запрос
    response_json = response.json()
    assert response_json.get("message") == "Недостаточно данных для создания учетной записи"






