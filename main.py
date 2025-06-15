from src import csv_excel_readers, external_api, generators, masks, processing, utils, widget

csv_transactions_check = csv_excel_readers.csv_reader("data/transactions.csv")
print(csv_transactions_check[:3])
excel_transactions_check = csv_excel_readers.excel_reader("data/transactions_excel.xlsx")
print(excel_transactions_check[:3])

try:
    transactions2 = utils.transactions_json_reader("data/operations2.json")
except FileNotFoundError:
    pass

transactions = utils.transactions_json_reader("data/operations.json")[:5:]
USD_transaction = transactions[0]

print(USD_transaction)

print(external_api.transaction_amount(USD_transaction))

print(widget.get_date("2024-03-11T02:26:18.671407"))
print(widget.mask_account_card("Счет 64686473678894779589"))
print(widget.mask_account_card("Visa Gold 5999414228426353"))
print(widget.mask_account_card("Maestro 1596837868705199"))

try:
    print(masks.get_mask_card_number(12341234123456))
except IndexError:
    pass
print(masks.get_mask_card_number(1234123412345687))


check_operation_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 41428839, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                        {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}]

# генерация номеров карт в диапазоне от start=12378568569997 до stop=12378568569999:
print(list(generators.card_number_generator(12378568569997, 12378568569999)))

# Фильтр по валюте операций из списка транзакций 'transactions' по доллару 'USD' и рублю 'RUB'
print(list(generators.filter_by_currency(transactions, "USD")))
print(list(generators.filter_by_currency(transactions, "RUB")))

# вывод деталей по операциям из списка транзакций 'transactions'
obtained_descriptions = generators.transaction_descriptions(transactions)
for index in range(len(transactions)):
    print(next(obtained_descriptions))

print(f"Успешные: {processing.filter_by_state(check_operation_list)}")
print(f"Отмененные: {processing.filter_by_state(check_operation_list, state='CANCELED')}")

print(f"Отсортированный по дате список операций:\n {processing.sort_by_date(check_operation_list)}")
print(f"В обратном порядке:\n {processing.sort_by_date(check_operation_list, is_reverse_order=False)}")
