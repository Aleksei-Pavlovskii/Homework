from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(list_dic: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    filter_state = []
    for dic in list_dic:
        if dic.get("state") == state:
            filter_state.append(dic)
    return filter_state


def sort_by_date(list_dic: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """ Функция, которая сортирует список по дате в порядке убывания """

    sorted_date = sorted(list_dic, key=lambda k: datetime.fromisoformat(k["date"]), reverse=reverse)
    return sorted_date
