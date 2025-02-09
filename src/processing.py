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
