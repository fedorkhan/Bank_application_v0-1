import pytest

from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(1234567812345678) == "1234 56** **** 5678")

#Проверка работоспособности функции 'get_mask_card_number()'
@pytest.mark.parametrize("card_number, mask", [
    (1234567812345678, "1234 56** **** 5678"),
    (1234567887654321, "1234 56** **** 4321"),
    ("1234567887654321", "1234 56** **** 4321")
])
def test_get_mask_card_number(card_number, mask):
    assert get_mask_card_number(card_number) == mask


with pytest.raises(IndexError) as card_length_error:
    get_mask_card_number(123456781234)

with pytest.raises(IndexError) as card_length_error:
    get_mask_card_number("")

#Проверка работоспособности функции 'get_mask_account()'
@pytest.mark.parametrize("account_number, mask", [
    (34567091367549208, "**9208"),
    (345670913890345, "**0345")
])
def test_get_mask_account(account_number, mask):
    assert get_mask_account(account_number) == mask


with pytest.raises(IndexError) as account_length_error:
    get_mask_account(12345)

with pytest.raises(IndexError) as account_length_error:
    get_mask_account("")