from src import csv_excel_readers, external_api, generators, processing, utils, widget


def main():
    """
    Отвечает за основную логику проекта и связывает функциональности между собой
    """

    # Запуск программы и считывание транзакций из файла
    while True:
        print(("Привет! Добро пожаловать в программу работы"
               "с банковскими транзакциями.\n"
               "Выберите необходимый пункт меню:\n"
               "1. Получить информацию о транзакциях из JSON-файла\n"
               "2. Получить информацию о транзакциях из CSV-файла\n"
               "3. Получить информацию о транзакциях из XLSX-файла"))

        user_get_transactions_input = input("Пользователь: ")

        if user_get_transactions_input == "1":
            print("Для обработки выбран JSON-файл")
            try:
                transactions = utils.transactions_json_reader("data/operations.json")
            except FileNotFoundError:
                print("Ошибка при чтении файла")
                continue

        elif user_get_transactions_input == "2":
            print("Для обработки выбран CSV-файл")
            try:
                transactions = csv_excel_readers.csv_reader("data/transactions.csv")
            except FileNotFoundError:
                print("Ошибка при чтении файла")
                continue

        elif user_get_transactions_input == "3":
            print("Для обработки выбран XLSX-файл")
            try:
                transactions = csv_excel_readers.excel_reader("data/transactions_excel.xlsx")
            except FileNotFoundError:
                print("Ошибка при чтении файла")
                continue
        else:
            print("некорректный ввод: введите 1, 2 или 3")
            continue
        break

    # Сортировка транзакций по статусу
    while True:
        print(("Введите статус, по которому необходимо выполнить фильтрацию.\n"
               "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"))
        user_status = input("Пользователь: ").upper()
        if user_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {user_status} недоступен.")
            continue
        else:
            filtered_by_state_transactions = processing.filter_by_state(transactions, state=user_status)
            print(f'Операции отфильтрованы по статусу "{user_status}"')
            break

    # Сортировка по дате в порядке возрастания или убывания
    print("Отсортировать операции по дате? Да/Нет")
    is_sort_by_date = input("Пользователь: ").capitalize() == "Да"

    if is_sort_by_date:
        try:
            print("Отсортировать по возрастанию или по убыванию?")
            sort_order = input("Пользователь: ").lower() == "по убыванию"
            sorted_by_date_transactions = processing.sort_by_date(filtered_by_state_transactions, sort_order)
        except Exception:
            print("Невозможно отсортировать транзакции по дате")
            sorted_by_date_transactions = filtered_by_state_transactions
    else:
        sorted_by_date_transactions = filtered_by_state_transactions

    print("Выводить только рублевые транзакции? Да/Нет")
    is_only_rubles = input("Пользователь: ").capitalize() == "Да"
    if is_only_rubles:
        try:
            currency_filtered_generator = generators.filter_by_currency(sorted_by_date_transactions,
                                                                        "RUB")
        except Exception:
            print("Невозможно применить фильтр по валюте")
            currency_filtered_transactions = sorted_by_date_transactions
        currency_filtered_transactions = list(currency_filtered_generator)
    else:
        currency_filtered_transactions = sorted_by_date_transactions

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    is_filter_by_description = input("Пользователь: ").capitalize() == "Да"
    if is_filter_by_description:
        print("Введите ключевое слово для поиска в описании")
        word_in_description = input("Пользователь: ")
        try:
            description_filtered_transactions = processing.process_bank_search(currency_filtered_transactions,
                                                                               word_in_description)
        except Exception:
            print(f"Невозможно отфильтровать список транзакций по слову '{word_in_description}'")
            description_filtered_transactions = currency_filtered_transactions
    else:
        description_filtered_transactions = currency_filtered_transactions

    print("Вывожу итоговый список транзакций...")
    if description_filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(description_filtered_transactions)}")
        # Форматированный вывод в консоль
        for transaction in description_filtered_transactions:
            print(f"{widget.get_date(transaction.get('date'))} {transaction.get('description')}")

            if type(transaction.get('from')) == str:
                print(f"{widget.mask_account_card(transaction.get('from'))} -> "
                      f"{widget.mask_account_card(transaction.get('to'))}")
            else:
                print(f"{widget.mask_account_card(transaction.get('to'))}")

            if type(transaction.get("operationAmount")) == dict:
                print(f"Сумма: {transaction.get('operationAmount').get('amount')} "
                      f"{transaction.get('operationAmount').get('currency').get('code')}\n")
            else:
                print(f"Сумма: {transaction.get('amount')} {transaction.get('currency_code')}\n")

            # Для работы с *.json файлами
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши"
              "условия фильтрации")

# print(external_api.transaction_amount(USD_transaction))


if __name__ == "__main__":
    main()
