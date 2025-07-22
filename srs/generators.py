from typing import Any, Dict, Generator, List


def filter_by_currency(my_list: List[Dict[str, Any]], currency: str) -> Generator:
    for i in my_list:
        currenc = i["operationAmount"]["currency"]["code"]
        if currenc == currency:
            yield i


def transaction_descriptions(my_list: List[Dict[str, Any]]) -> Generator:
    for i in my_list:
        desc = i["description"]
        yield desc


def card_number_generator(start: int, stop: int) -> Generator:
    stop += 1
    for i in range(start, stop):
        nums = str(i).zfill(16)
        if len(nums) <= 16:
            yield f"{nums[0:4]} {nums[4:8]} {nums[8:12]} {nums[12:]}"
