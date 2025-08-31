import re
from collections import Counter
from datetime import datetime
from typing import Any, Dict, List

data = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_state(list_dic: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    filter_state = []
    for dic in list_dic:
        if dic.get("state") == state:
            filter_state.append(dic)
    return filter_state


def sort_by_date(list_dic: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция, которая сортирует список по дате в порядке убывания"""

    sorted_date = sorted(list_dic, key=lambda k: datetime.fromisoformat(k["date"]), reverse=reverse)
    return sorted_date


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [transaction for transaction in data if pattern.findall(transaction["description"])]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи это названия категорий, а значения это количество операций.
    """

    return dict(
        Counter(transaction["description"] for transaction in data if transaction["description"] in categories)
    )
