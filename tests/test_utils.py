from unittest.mock import mock_open, patch

from src.utils import transactions_json_reader


def test_transactions_json_reader_success():
    check_transaction = """
    [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]"""

    with patch('builtins.open', mock_open(read_data=check_transaction)):
        assert transactions_json_reader("data/test_operation.json") == [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]


def test_transactions_json_reader_bad_data():
    check_transaction = """
    [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        ]"""

    with patch('builtins.open', mock_open(read_data=check_transaction)):
        assert transactions_json_reader("data/test_operation.json") == []


def test_transactions_json_file_not_found():
    assert transactions_json_reader("data/operations_that_not_exist.json") == []
