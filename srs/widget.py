from srs.masks import get_mask_account


def mask_account_card(account_number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""

    card_name = []
    card_namber_split = account_number.split(" ")
    join_card_number = "".join(card_namber_split[-1])
    for i in card_namber_split:
        if i == "Счет":
            card_name.append(i)
            return f"{" ".join(card_name)} {get_mask_account(account_number)}"
        else:
            pass
        for i in card_namber_split:
            if i.isalpha():
                card_name.append(i)
        return f"{" ".join(card_name)} {join_card_number[0:4]} {join_card_number[4:6]}** **** {join_card_number[-4:]}"


def get_date(user_data: str) -> str:
    """Функция, которая принимает дату пользователя и возвращает дату в формате 'ДД.ММ.ГГГГ'"""

    data_part = user_data.split("T")[0]
    times = data_part.split("-")[::-1]
    format_data = ".".join(times)
    return format_data
