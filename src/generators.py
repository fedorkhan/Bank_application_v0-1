from typing import Iterator, Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Iterator:
    """
    Принимает на вход список словарей, представляющих транзакции
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    :param transactions_list: list[dict]
    :param currency: int
    :return:
    """
    for transaction in transactions_list:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Iterator:
    """
    Принимает список словарей с транзакциями.
    Возвращает описание каждой операции по очереди.
    Если на вход подается пустой список транзакций или ни у одной из транзакций нет описания,
    выбрасывается StopIteration
    :param transactions_list:
    :return:
    """
    for transaction in transactions_list:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Принимает начальное 'start' и конечное 'stop' значения для генерации диапазона номеров.
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    :param start:
    :param stop:
    :return:
    """
    for number in range(start, stop + 1):
        raw_card_number = '0' * (16 - len(str(number))) + str(number)
        card_number = []

        for index in range(len(raw_card_number)):
            card_number.append(raw_card_number[index])
            if (index + 1) % 4 == 0:
                card_number.append(' ')
        yield "".join(card_number)[:-1:]
