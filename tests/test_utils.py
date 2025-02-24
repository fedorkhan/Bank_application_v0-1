import json
from unittest.mock import Mock

from src.utils import transactions_json_reader


def test_transactions_json_reader():
    """
    Тест функции transactions_json_reader
    """
    mock_load = Mock(return_value=[
        {
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
        }
    ])
    json.load = mock_load
    assert transactions_json_reader("data/operations.json") == [{
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
    mock_load.assert_called_once()


def test_transactions_json_file_not_found():
    assert transactions_json_reader("data/operations_that_not_exist.json") == []
