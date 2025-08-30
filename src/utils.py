import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.filter_data import filter_data_file

load_dotenv()

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(filename: str | None = None) -> Any | list:
    """Функция, которая проверяет наличие файла и читает его"""
    try:
        if filename and os.path.exists(filename):
            with open(filename, encoding="utf-8") as f:
                data = filter_data_file(json.load(f))
            logger.info(f"Файл {data} найден")
            return data
        else:
            logger.warning(f"Файл {filename} не найден")
            return []
    except Exception as err:
        logger.setLevel(logging.ERROR)
        logger.error(f"Произошла ошибка {err}")
        return "Произошла ошибка"


def currency_conversion(transactions: list[dict]) -> float | str:
    """Функция, которая конвертирует валюту и возвращает сумму операций"""
    amount = []
    try:
        logger.info("Запущен процесс конвертации валюты в транзакциях")
        for transaction in transactions:
            trans_code = transaction["operationAmount"]["currency"]["code"]
            if trans_code == "RUB":
                amount.append(float(transaction["operationAmount"]["amount"]))
            else:
                base_url = "https://api.apilayer.com/exchangerates_data/convert"
                url = f"{base_url}?to={"RUB"}&from={trans_code}&amount={transaction['operationAmount']['amount']}"
                token_api = os.getenv("API_KEY")
                payload: dict = {}
                headers = {"apikey": token_api}

                response = requests.get(url, headers=headers, data=payload)

                results = response.json()
                amount.append(float(results["result"]))
        logger.info(f"Процесс завершен, сумма транзакций {round(sum(amount), 2)}")
        return round(sum(amount), 2)
    except Exception as err:
        logger.setLevel(logging.ERROR)
        logger.error(f"Произошла ошибка {err}")
        return "Ошибка при обработке транзакций"
