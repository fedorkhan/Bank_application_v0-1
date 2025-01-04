import os

if os.path.exists("masks.py"):
    import masks
elif os.path.exists("src/masks.py"):
    from src import masks


def mask_account_card(card_account_info: str) -> str:
    """
    Принимает строку, содержащую тип и номер карты или счета
    Возвращает строку с замаскированным номером
    :param card_account_info: str
    :return: str
    """
    separated_info = card_account_info.split(" ")
    number = int(separated_info[-1])
    name = separated_info[:-1:]

    if "Счет" in name:
        masked_number = masks.get_mask_account(number)
    else:
        masked_number = masks.get_mask_card_number(number)

    return " ".join([*name, masked_number])


def get_date(time_info: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    Возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")
    :param time_info: str
    :return: str
    """
    date, time = time_info.split("T")
    year, month, day = date.split("-")

    formatted_date = ".".join([day, month, year])

    return formatted_date


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Maestro 1596837868705199"))
