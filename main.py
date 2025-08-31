from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.read_csv_xlsx_files import read_csv_file, read_xlsx_file
from src.utils import read_json_file
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    print(
        """
Привет! Добро пожаловать в программу работы с банковскими транзакциями
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    """
    )
    user_input = input()
    file: list[dict] = []
    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        file = read_json_file("data/operations.json")
    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        file = read_csv_file("data/transactions.csv")
    elif user_input == "3":
        print("Для обработки выбран XLSX-файл")
        file = read_xlsx_file("data/transactions_excel.xlsx")

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        user_state = input().upper()
        if user_state in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {user_state}")
            filter_state = filter_by_state(file, user_state)
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_sort_date = input().lower()
        if user_sort_date == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                user_sort_ascending = input().lower()
                if user_sort_ascending == "по возрастанию":
                    sort_by_ascending_order = sort_by_date(filter_state, reverse=False)
                    break
                elif user_sort_ascending == "по убыванию":
                    sort_by_ascending_order = sort_by_date(filter_state)
                    break
                else:
                    print("Неверный выбор. Попробуйте еще раз.")
            break
        elif user_sort_date == "нет":
            sort_by_ascending_order = filter_state
            break
        else:
            print('Ответьте "Да" или "Нет"')

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_sort_rub = input().lower()
        if user_sort_rub == "да":
            rub_transactions = []
            for transaction in sort_by_ascending_order:
                if transaction["currency_code"] == "RUB":
                    rub_transactions.append(transaction)
            filter_transaction = rub_transactions
            break
        elif user_sort_rub == "нет":
            filter_transaction = sort_by_ascending_order
            break

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_specific_word = input().lower()
        if user_specific_word == "да":
            print("Введите слово по которому фильтровать")
            user_word = input()
            filter_transaction = process_bank_search(filter_transaction, user_word)
            break
        elif user_specific_word == "нет":
            filter_transaction = filter_transaction
            break
        else:
            print('Ответьте "Да" или "Нет"')

    if not filter_transaction:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        for sort_transaction in filter_transaction:
            amount = sort_transaction.get("amount")
            currency_code = sort_transaction.get("currency_code")
            currency_name = sort_transaction.get("currency_name")
            date = sort_transaction.get("date")
            description = sort_transaction.get("description")
            from_trans = sort_transaction.get("from")
            to_trans = sort_transaction.get("to")
            id_trans = sort_transaction.get("id")
            state = sort_transaction.get("state")
            if description == "Открытие вклада":
                print(
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(to_trans)}\n"
                    f"Сумма: {amount} {currency_code}\n"
                )
            else:
                print(
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(from_trans)} -> {mask_account_card(to_trans)}\n"
                    f"Сумма: {amount} {currency_code}\n"
                )
