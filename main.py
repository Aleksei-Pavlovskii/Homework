from srs.masks import get_mask_account, get_mask_card_number

# Запрашиваем у пользователя номер карты и номер счета
card_number = input("Введите номер карты: ")
account_number = input("Введите номер счёта: ")

# Вызываем функцию, которая маскирует номер карты
print(get_mask_card_number(card_number))
# Вызываем функцию, которая маскирует номер счёта
print(get_mask_account(account_number))
