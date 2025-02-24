import json


def transactions_json_reader(filename: str) -> [dict]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список
    """

    try:
        with open(filename, "r", encoding="utf-8") as transactions_file:
            transactions = json.load(transactions_file)
    except Exception:
        transactions = []

    return transactions
