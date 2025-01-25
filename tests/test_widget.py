import pytest


from src.widget import get_date, mask_account_card
from tests.conftest import time_example1, date_example1, date_example2, time_example2

#Проверка функции 'get_date' при помощи фикстур
def test_get_date1(time_example1, date_example1):
    assert get_date(time_example1) == date_example1

def test_get_date2(time_example2, date_example2):
    assert get_date(time_example2) == date_example2

with pytest.raises(ValueError) as WrongTimeFormat:
    get_date("2024.03.11T02:26:18.671407")

with pytest.raises(ValueError) as WrongTimeFormat2:
    get_date("")

#Проверка функции mask_account_card()
@pytest.mark.parametrize("card_account_info, masked_card_account", [
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 646864736788947", "Счет **8947"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("5999414228426353", "5999 41** **** 6353")
])
def test_mask_account_card(card_account_info, masked_card_account):
    assert mask_account_card(card_account_info) == masked_card_account

with pytest.raises(IndexError) as WrongCardNumber:
    mask_account_card("Visa Gold 59994142284263")

with pytest.raises(IndexError) as WrongAccountNumber:
    mask_account_card("Счет 5999")