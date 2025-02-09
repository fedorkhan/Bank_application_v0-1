import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тестирование функции card_number_generator()
@pytest.mark.parametrize("start, stop, card_numbers", [
    (12, 13, ["0000 0000 0000 0012", "0000 0000 0000 0013"]),
    (88005553535, 88005553538, ["0000 0880 0555 3535", "0000 0880 0555 3536",
                                "0000 0880 0555 3537", "0000 0880 0555 3538"])
])
def test_card_number_generator(start: int, stop: int, card_numbers: list[str]) -> None:
    """Функция для проверки работы card_number_generator() из модуля 'generators'
        Работа при условии корректно заданных входных данных"""
    card_numbers_generated = card_number_generator(start, stop)
    for index in range(0, stop - start + 1):
        assert next(card_numbers_generated) == card_numbers[index]


with pytest.raises(StopIteration):
    """Проверка работы card_number_generator() из модуля 'generators'
        Попытка обратиться к элементам вне диапазона 'start' < number < 'stop'
        вызывает исключение StopIteration"""
    card_numbers_generated = card_number_generator(2025, 2025)
    next(card_numbers_generated)
    next(card_numbers_generated)


# Тестирование функции filter_by_currency()
def test_filter_by_currency_usd(transactions_list_example: list[dict], usd_transactions: list) -> None:
    """Функция для проверки работы filter_by_currency() из модуля 'generators'
        Возвращаются долларовые транзакции"""
    assert list(filter_by_currency(transactions_list_example, "USD")) == usd_transactions


def test_filter_by_currency_rub(transactions_list_example: list[dict], rub_transactions: list) -> None:
    """Функция для проверки работы filter_by_currency() из модуля 'generators'
        Возвращаются рублевые транзакции"""
    assert list(filter_by_currency(transactions_list_example, "RUB")) == rub_transactions


def test_filter_by_currency_unknown(transactions_list_example: list[dict]) -> None:
    """Функция для проверки работы filter_by_currency() из модуля 'generators'
        Вывод транзакций, валюты которых нет в базе"""
    assert list(filter_by_currency(transactions_list_example, "EUR")) == []


def test_filter_by_currency_bad_data() -> None:
    """Функция для проверки работы filter_by_currency() из модуля 'generators'
        Случай, когда на входе пустой список транзакций"""
    assert list(filter_by_currency([], "USD")) == []


# Тестирование функции filter_by_currency()
def test_transaction_descriptions(transactions_list_example: list[dict], descriptions: list[str]) -> None:
    """Функция для проверки работы transaction_descriptions() из модуля 'generators'
        Проверка при нормальных условиях"""
    obtained_descriptions = transaction_descriptions(transactions_list_example)
    for index in range(len(transactions_list_example)):
        assert next(obtained_descriptions) == descriptions[index]


def test_transaction_descriptions_empty() -> None:
    """Функция для проверки работы transaction_descriptions() из модуля 'generators'
        Если на вход подается пустой список транзакций или ни у одной из транзакций нет описания,
        выбрасывается StopIteration"""
    with pytest.raises(StopIteration):
        obtained_descriptions = transaction_descriptions([])
        assert next(obtained_descriptions)
