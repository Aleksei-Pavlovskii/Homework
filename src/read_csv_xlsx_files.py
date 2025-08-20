import pandas as pd


def read_csv_file(filename_csv: str) -> list[dict]:
    """Функция, которая читает csv файл"""
    file_csv = pd.read_csv(filename_csv, delimiter=";")
    return file_csv.to_dict("records")


def read_xlsx_file(filename_xlsx: str) -> list[dict]:
    """Функция, которая читает xlsx файл"""
    file_xlsx = pd.read_excel(filename_xlsx)
    return file_xlsx.to_dict("records")
