from srs.generators import filter_by_currency, transaction_descriptions, card_number_generator
from srs.widget import get_date, mask_account_card


# Запрашиваем у пользователя номер карты и номер счета
account_number = input("Введите номер карты или счета: ")
user_data = input("Введите дату: ")

# Вызываем функцию, которая маскирует номер карты
print(mask_account_card(account_number))
print(get_date(user_data))

usd_transactions = filter_by_currency(transactions, "USD")
for i in range(4):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Нет больше транзакций в указанной валюте")
        break

descriptions = transaction_descriptions(transactions)
for desc in range(10):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Нет больше финансовых операций")
        break

for card_number in card_number_generator(1, 5):
    print(card_number)