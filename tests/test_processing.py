from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state(list_dict):
    assert filter_by_state(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state([]) == []


def test_sort_by_date(list_dict):
    assert sort_by_date(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date([]) == []


def test_process_bank_search(data_file):
    expected = [
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

    word = "организации"
    result = process_bank_search(data_file, word)
    assert result == expected


def test_process_bank_operations(data_file):
    expected = {"Перевод организации": 1}
    assert process_bank_operations(data_file, "Перевод организации") == expected
