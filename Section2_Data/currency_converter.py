import requests
import os
import dotenv 

dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')

url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/RUB'

response = requests.get(url)
data = response.json()

def currency_converter(rubles, currency):
    try:
        return f"{rubles*data["conversion_rates"][currency]:.2f}"
    except KeyError:
        return "Ошибка: Пожалуйста, введите корректное наименование валюты: https://www.exchangerate-api.com/docs/supported-currencies"
    except ZeroDivisionError:
        return "Ошибка: Курс валюты не может быть нулевым"

currency = input(f"Введите нужную вам валюту (USD, EUR, CNY and ect.): ").upper()

try:
    rub_amount = float(input("Введите сумму в рублях: "))
except ValueError:
    print("Ошибка: Введите число для суммы")
    exit()

print(f"Результат: {currency_converter(rub_amount, currency)} {currency}")