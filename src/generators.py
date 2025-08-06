from typing import Any, Dict, Generator, List


def filter_by_currency(my_list: List[Dict[str, Any]], currency: str) -> Generator:
    """Генератор, который поочередно выдает транзакции"""
    for i in my_list:
        currenc = i["operationAmount"]["currency"]["code"]
        if currenc == currency:
            yield i


def transaction_descriptions(my_list: List[Dict[str, Any]]) -> Generator:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for i in my_list:
        desc = i["description"]
        yield desc


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор, который выдает номера банковских карт"""
    stop += 1
    for i in range(start, stop):
        nums = str(i).zfill(16)
        if len(nums) <= 16:
            yield f"{nums[0:4]} {nums[4:8]} {nums[8:12]} {nums[12:]}"
