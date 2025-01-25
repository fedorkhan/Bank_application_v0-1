def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде 16-значного числа.
    Возвращает маску по правилу: XXXX XX** **** XXXX
    Вызывает исключение 'IndexError', если номер карты состоит не из 16 цифр
    :param card_number: int
    :return: str
    """
    if len(str(card_number)) != 16:
        raise IndexError("В номере карты не 16 цифр")

    masked_card_digits_list = []

    for index in range(len(str(card_number))):
        if 6 <= index <= 11:
            masked_card_digits_list.append("*")
        else:
            masked_card_digits_list.append(str(card_number)[index])

        if (index + 1) % 4 == 0:
            masked_card_digits_list.append(" ")

    return "".join(masked_card_digits_list)[:-1:]


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета в виде числа.
    Возвращает маску номера по правилу **XXXX
    Вызывает исключение 'IndexError', если длина счета менее 6 цифр
    :param account_number: int
    :return: str
    """
    if len(str(account_number)) < 6:
        raise IndexError("В номере счета менее 6 цифр")

    account_last_six_digits = str(account_number)[-6::]
    masked_account_digits_list = []
    for index in range(len(account_last_six_digits)):
        if index < 2:
            masked_account_digits_list.append("*")
        else:
            masked_account_digits_list.append(account_last_six_digits[index])

    return "".join(masked_account_digits_list)


if __name__ == "__main__":
    print(get_mask_card_number(1234567812345678))
    print(get_mask_account(34567091367549208))
