from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


# Проверка функции 'filter_by_state()'
def test_filter_by_state_executed(operations_list_example: list, executed_operations: list) -> None:
    assert filter_by_state(operations_list_example, 'EXECUTED') == executed_operations


def test_filter_by_state_canceled(operations_list_example: list, canceled_operations: list) -> None:
    assert filter_by_state(operations_list_example, 'CANCELED') == canceled_operations


def test_filter_by_state_unknown(operations_list_example: list, unknown_operations: list) -> None:
    assert filter_by_state(operations_list_example, 'INTERRUPTED') == unknown_operations
    assert filter_by_state(operations_list_example, 'UNKNOWN') == unknown_operations


# Проверка функции 'sort_by_date()'
def test_sort_by_date(operations_list_example: list, sorted_operations_list_example: list) -> None:
    assert sort_by_date(operations_list_example) == sorted_operations_list_example


def test_reverse_sort_by_date(operations_list_example: list, reverse_sorted_operations_list_example: list) -> None:
    assert sort_by_date(operations_list_example, is_reverse_order=False) == reverse_sorted_operations_list_example


# Проверка функции 'process_bank_search()'
def test_process_bank_search(operations_list_example: list, found_operations_list_example: list):
    assert process_bank_search(operations_list_example, "Перевод организации") == found_operations_list_example


def test_process_bank_search_wrong(operations_list_example: list):
    assert process_bank_search(operations_list_example, "Перевод в организацию") == []


# Проверка функции 'process_bank_operations()'
def test_process_bank_operations(operations_list_example: list, categorized_data: dict):
    assert (process_bank_operations(operations_list_example, ["Перевод организации", "Открытие вклада"]) ==
            categorized_data)


def test_process_bank_operations_failed(operations_list_example: list):
    assert process_bank_operations(operations_list_example, []) == {}
