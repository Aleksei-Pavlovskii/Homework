from src.filter_data import filter_data_file


def test_filter_data_file():
    data_file = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]

    expected = [
        {
            "amount": "9824.07",
            "currency_code": "USD",
            "currency_name": "USD",  # Обратите внимание: в исходных данных name тоже "USD"
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        }
    ]
    result = filter_data_file(data_file)
    assert result == expected
