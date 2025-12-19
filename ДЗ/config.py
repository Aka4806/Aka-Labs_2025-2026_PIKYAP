import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', '8533845301:AAFa7nrDS8IARkRrtPDeX8rSJuBd563nW1M')

API_KEY = os.getenv('API_KEY', 'YOUR_API_KEY_HERE')

BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

POPULAR_CURRENCIES = [
    'USD', 'EUR', 'GBP', 'JPY', 'CAD',
    'AUD', 'CHF', 'CNY', 'RUB', 'UAH'
]