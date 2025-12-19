import requests
import json
from config import BASE_URL, API_KEY


class CurrencyConverter:
    def __init__(self):
        self.cache = {}
        self.cache_timeout = 3600

    def get_exchange_rates(self, base_currency):
        try:
            url = f"{BASE_URL}{base_currency}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data.get('result') == 'error':
                return None

            return data['rates']

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении курсов валют: {e}")
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        try:
            rates = self.get_exchange_rates(from_currency)
            if not rates or to_currency not in rates:
                return None

            rate = rates[to_currency]
            converted_amount = amount * rate
            return converted_amount

        except Exception as e:
            print(f"Ошибка при конвертации: {e}")
            return None

    def get_available_currencies(self):
        rates = self.get_exchange_rates('USD')
        if rates:
            return list(rates.keys())
        return []

converter = CurrencyConverter()