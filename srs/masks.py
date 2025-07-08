def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает номер карты и возвращает маску номера"""

    if len(card_number) == 16:
        return f"{str(card_number)[0:6]}** ****  {str(card_number)[12:]}"
    else:
        return "Некоректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает номер счета и возвращает маску номера"""

    if len(account_number) >= 4:
        return f"**{str(account_number)[-4:]}"
    else:
        return "Некоректный номер счёта"
