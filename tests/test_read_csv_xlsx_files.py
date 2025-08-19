from unittest.mock import patch

from src.read_csv_xlsx_files import read_csv_file, read_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_csv) -> None:

    mock_csv.return_value.to_dict.return_value = [
        {"id": 650703, "state": "EXECUTED"},
        {"id": 3598919, "state": "EXECUTED"},
    ]
    assert read_csv_file("test.csv") == [{"id": 650703, "state": "EXECUTED"}, {"id": 3598919, "state": "EXECUTED"}]


@patch("pandas.read_excel")
def test_read_xlsx_file(mock_xlsx) -> None:

    mock_xlsx.return_value.to_dict.return_value = [
        {"id": 650703, "state": "EXECUTED"},
        {"id": 3598919, "state": "EXECUTED"},
    ]
    assert read_xlsx_file("test.xlsx") == [{"id": 650703, "state": "EXECUTED"}, {"id": 3598919, "state": "EXECUTED"}]
