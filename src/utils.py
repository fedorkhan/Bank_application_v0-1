import json
import logging

logger_utils = logging.getLogger("utils")
logger_utils.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)


def transactions_json_reader(filename: str) -> [dict]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список
    """
    logger_utils.info(f"Начало работы функции transactions_json_reader({filename})")

    try:
        with open(filename, "r", encoding="utf-8") as transactions_file:
            transactions = json.load(transactions_file)
    except FileNotFoundError as file_err:
        logger_utils.error(f"Файл не найден: {file_err}")
        transactions = []
    except json.decoder.JSONDecodeError as js_err:
        logger_utils.error(f"Ошибка при декодировании .json-файла: {js_err}")
        transactions = []
    except Exception as e:
        logger_utils.error(f"Ошибка при чтении файла: {e}")
        transactions = []

    logger_utils.info(f"Завершение работы функции transactions_json_reader({filename})")

    return transactions
