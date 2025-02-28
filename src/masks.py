import logging

logger1 = logging.getLogger("masks")
logger1.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger1.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде 16-значного числа.
    Возвращает маску по правилу: XXXX XX** **** XXXX
    Вызывает исключение 'IndexError', если номер карты состоит не из 16 цифр
    :param card_number: int
    :return: str
    """

    logger1.info(f"Начало работы функции `get_mask_card_number({card_number})`")

    if len(str(card_number)) != 16:
        logger1.critical("В номере карты не 16 цифр. Дальнейшая работа функции невозможна")
        raise IndexError("В номере карты не 16 цифр")

    masked_card_digits_list = []
    logger1.info("В номере карты 16 цифр. Запуск процедуры маскировки")

    for index in range(len(str(card_number))):
        if 6 <= index <= 11:
            masked_card_digits_list.append("*")
        else:
            masked_card_digits_list.append(str(card_number)[index])

        if (index + 1) % 4 == 0:
            masked_card_digits_list.append(" ")

    masked_card = "".join(masked_card_digits_list)[:-1:]
    logger1.info("Успешное завершение работы функции `get_mask_card_number()`\n" +
                 masked_card)

    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета в виде числа.
    Возвращает маску номера по правилу **XXXX
    Вызывает исключение 'IndexError', если длина счета менее 6 цифр
    :param account_number: int
    :return: str
    """
    logger1.info(f"Начало работы функции `get_mask_account({account_number})`")

    if len(str(account_number)) < 6:
        logger1.critical("В номере счета менее 6 цифр. Дальнейшая работа функции невозможна")
        raise IndexError("В номере счета менее 6 цифр")

    account_last_six_digits = str(account_number)[-6::]
    masked_account_digits_list = []
    for index in range(len(account_last_six_digits)):
        if index < 2:
            masked_account_digits_list.append("*")
        else:
            masked_account_digits_list.append(account_last_six_digits[index])
    masked_account = "".join(masked_account_digits_list)
    logger1.info("Успешное завершение работы функции `get_mask_account()`\n" +
                 masked_account)

    return masked_account
