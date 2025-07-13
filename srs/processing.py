from typing import Any, Dict, List


def filter_by_state(list_dic: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    filter_state = []
    for dic in list_dic:
        if dic.get("state") == state:
            filter_state.append(dic)
    return filter_state

