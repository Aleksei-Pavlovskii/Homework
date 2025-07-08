from srs.widget import get_date, mask_account_card

# Запрашиваем у пользователя номер карты и номер счета
account_number = input("Введите номер карты или счета: ")
user_data = input("Введите дату: ")

# Вызываем функцию, которая маскирует номер карты
print(mask_account_card(account_number))
print(get_date(user_data))
