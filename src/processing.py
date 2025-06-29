import re
from collections import Counter


def filter_by_state(operations_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED')
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    :param operations_list: list[dict]
    :param state: str
    :return: filtered_operations_list -> list[dict]
    """
    filtered_operations_list = []

    for operation in operations_list:
        if 'state' not in operation.keys():
            continue

        if operation['state'] == state:
            filtered_operations_list.append(operation)

    return filtered_operations_list


def sort_by_date(operations_list: list[dict], is_reverse_order: bool = True) -> list[dict]:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Возвращает новый список, отсортированный по дате (date)
    :param operations_list: list[dict]
    :param is_reverse_order: bool
    :return: list[dict]
    """

    sorted_operations_list = sorted(operations_list, key=lambda x: x['date'], reverse=is_reverse_order)

    return sorted_operations_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    """
    found_operations = [transaction for transaction in data if re.search(search, transaction["description"].lower())]

    return found_operations


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    """
    counted_operations = Counter([transaction["description"] for transaction in data
                                  if transaction["description"] in categories])

    return dict(counted_operations)
