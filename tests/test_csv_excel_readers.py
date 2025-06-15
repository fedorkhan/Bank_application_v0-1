from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.csv_excel_readers import csv_reader, excel_reader


@patch('pandas.read_excel')
def test_excel_reader_success(mock_get):
    """
    Проверка работы функции 'csv_reader()' из модуля 'csv_excel_readers.py'
    в успешном случае
    """

    mock_get.return_value = pd.DataFrame({
        'id': [650703.0],
        'state': ['EXECUTED'],
        'date': ['2023-09-05T11:30:32Z'],
        'amount': [16210.0],
        'currency_name': ['Sol'],
        'currency_code': ['PEN'],
        'from': ['Счет 58803664561298323391'],
        'to': ['Счет 39745660563456619397'],
        'description': ['Перевод организации']
    })

    assert excel_reader("data/transactions_excel.xlsx") == [
        {
            'id': 650703.0,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }]


def test_excel_reader_file_not_found():
    """
    Проверка работы функции 'csv_reader()' из модуля 'csv_excel_readers.py'
    в случае, когда файл не найден
    """
    with pytest.raises(FileNotFoundError):
        excel_reader("data/transactions_excel_that_do_not_exist.xlsx")


def test_csv_reader_success():
    """
    Проверка работы функции 'csv_reader()' из модуля 'csv_excel_readers.py'
    в успешном случае
    """

    check_transactions = """id;state;date;amount;currency_name;currency_code;from;to;description
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"""

    with patch('builtins.open', mock_open(read_data=check_transactions)):
        assert csv_reader("data/transactions.csv") == [{
            'id': 3598919.0,
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z',
            'amount': 29740.0,
            'currency_name': 'Peso',
            'currency_code': 'COP',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'
        }]


def test_csv_reader_file_not_found():
    """
    Проверка работы функции 'csv_reader()' из модуля 'csv_excel_readers.py'
    в случае, когда файл не найден
    """
    with pytest.raises(FileNotFoundError):
        csv_reader("data/transactions_that_do_not_exist.csv")
