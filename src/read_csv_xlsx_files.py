import pandas as pd

from src.filter_data import filter_data_file


def read_csv_file(filename_csv: str) -> list[dict]:
    """Функция, которая читает csv файл"""
    file_csv = pd.read_csv(filename_csv, delimiter=";")
    return filter_data_file(file_csv.to_dict("records"))


def read_xlsx_file(filename_xlsx: str) -> list[dict]:
    """Функция, которая читает xlsx файл"""
    file_xlsx = pd.read_excel(filename_xlsx)
    return filter_data_file(file_xlsx.to_dict("records"))
