import datetime
from faker import Faker
import random

fake = Faker()
def generate_order(): #(colors=None)
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 100),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 5),
        "deliveryDate": datetime.datetime.today().strftime('%Y-%m-%d'),
        "comment": fake.sentence(),
        "color": [random.choice(["BLACK", "GREY"])] #  "color": [color] if color else []  # Если цвет указан, добавляем его, иначе пустой список
    }

def generate_courier(): # создать нового курьера
    return {
        "login": fake.unique.user_name(),  # Уникальный логин
        "password": fake.password(length=4),  # Случайный пароль
        "firstName": fake.first_name()  # Случайное имя
    }