from src.read_csv_xlsx_files import read_csv_file, read_xlsx_file

if __name__ == "__main__":
    print(read_csv_file("data/transactions.csv"))
    print(read_xlsx_file("data/transactions_excel.xlsx"))
