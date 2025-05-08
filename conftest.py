import allure
import pytest
import requests
from curl import url

@allure.step("Фикстура создает курьера,а потом его удаляет по id")
@pytest.fixture
def courier_cleanup():
    courier_ids = []
    def register_courier_for_cleanup(courier_id):
        courier_ids.append(courier_id)

    yield register_courier_for_cleanup

    for courier_id in courier_ids:
        delete_response = requests.delete(f"{url.DELETE_COURIER}/{courier_id}")
        assert delete_response.status_code == 200, f"Ошибка удаления: {delete_response.text}"
        delete_response_json = delete_response.json()
        assert delete_response_json.get("ok") is True, "Ошибка: курьер не удалён!"



