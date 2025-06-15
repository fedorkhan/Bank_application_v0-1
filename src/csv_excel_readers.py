import pandas as pd


def csv_reader(filename: str) -> list[dict]:
    """
    Принимает путь к файлу CSV в качестве аргумента.
    Выдает список словарей с транзакциями.
    """
    with open(filename, "r", encoding="utf-8") as file_csv:
        csv_transactions_df = pd.read_csv(file_csv, delimiter=';')

    csv_transactions_list = csv_transactions_df.to_dict("records")

    return csv_transactions_list


def excel_reader(filename: str) -> list[dict]:
    """
    Принимает путь к файлу EXCEL в качестве аргумента.
    Выдает список словарей с транзакциями
    """
    excel_transactions_df = pd.read_excel(filename)

    excel_transactions_list = excel_transactions_df.to_dict("records")

    return excel_transactions_list
