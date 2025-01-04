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


if __name__ == '__main__':
    check_operation_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print(f"Успешные: {filter_by_state(check_operation_list)}")
    print(f"Отмененные: {filter_by_state(check_operation_list, state='CANCELED')}")
    print(f"Отсортированный по дате список операций:\n {sort_by_date(check_operation_list)}")
