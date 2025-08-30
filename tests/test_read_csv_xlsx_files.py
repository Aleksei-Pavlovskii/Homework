from unittest.mock import patch

from src.read_csv_xlsx_files import read_csv_file, read_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_csv) -> None:

    mock_csv.return_value.to_dict.return_value = [
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 650703,
            "state": "EXECUTED",
            "to": None,
        },
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 3598919,
            "state": "EXECUTED",
            "to": None,
        },
    ]
    expected = [
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 650703,
            "state": "EXECUTED",
            "to": None,
        },
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 3598919,
            "state": "EXECUTED",
            "to": None,
        },
    ]
    assert read_csv_file("test.csv") == expected


@patch("pandas.read_excel")
def test_read_xlsx_file(mock_xlsx) -> None:

    mock_xlsx.return_value.to_dict.return_value = [
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 650703,
            "state": "EXECUTED",
            "to": None,
        },
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 3598919,
            "state": "EXECUTED",
            "to": None,
        },
    ]
    expected = [
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 650703,
            "state": "EXECUTED",
            "to": None,
        },
        {
            "amount": None,
            "currency_code": {},
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": 3598919,
            "state": "EXECUTED",
            "to": None,
        },
    ]
    assert read_xlsx_file("test.xlsx") == expected
