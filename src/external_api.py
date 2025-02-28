import os
from json import loads

import dotenv
import requests


def transaction_amount(transaction):
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях, тип данных — float
    Если транзакция была в USD, EUR или любой другой иностранной валюте, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    Для конвертации валюты используется Exchange Rates Data API
    """
    currency = transaction.get("operationAmount").get("currency").get("code")
    currency_amount = float(transaction.get("operationAmount").get("amount"))
    if currency == "RUB":
        return currency_amount
    else:
        try:
            if currency_amount is not None:
                api_url = "https://api.apilayer.com/exchangerates_data/latest"
                dotenv.load_dotenv()

                api_key = os.getenv('API_KEY')
                headers = {
                    "apikey": api_key
                }

                params = {
                    "symbols": currency,
                    "base": "RUB",
                }

                api_response = requests.get(url=api_url, headers=headers, params=params)
                status_code = api_response.status_code

                if status_code != 200:
                    raise Exception("Cannot reach the server")

                conversion_rate = 1.0 / float(loads(api_response.text).get("rates").get(currency))

                return round(conversion_rate * currency_amount, 2)
            else:
                raise ValueError("No 'amount' data of the transaction")

        except ValueError:
            return 0
