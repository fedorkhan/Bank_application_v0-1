from unittest.mock import patch

from src.external_api import transaction_amount


def test_transaction_amount_rub(rub_transactions):
    assert transaction_amount(rub_transactions[0]) == 43318.34


@patch('requests.get')
def test_transaction_amount_usd(mock_get, usd_transactions):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = '{"rates": {"USD": "0.0125"}}'

    assert transaction_amount(usd_transactions[0]) == 9824.07 * 80.0
