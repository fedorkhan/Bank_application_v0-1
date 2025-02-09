from src import generators, processing, widget

print(widget.get_date("2024-03-11T02:26:18.671407"))
print(widget.mask_account_card("Счет 64686473678894779589"))
print(widget.mask_account_card("Visa Gold 5999414228426353"))
print(widget.mask_account_card("Maestro 1596837868705199"))

check_operation_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 41428839, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                        {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}]

transactions = [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]

#генерация номеров карт в диапазоне от start=12378568569997 до stop=12378568569999:
print(list(generators.card_number_generator(12378568569997, 12378568569999)))

#Фильтр по валюте операций из списка транзакций 'transactions' по доллару 'USD' и рублю 'RUB'
print(list(generators.filter_by_currency(transactions, "USD")))
print(list(generators.filter_by_currency(transactions, "RUB")))

#вывод деталей по операциям из списка транзакций 'transactions'
obtained_descriptions = generators.transaction_descriptions(transactions)
for index in range(len(transactions)):
    print(next(obtained_descriptions))

print(f"Успешные: {processing.filter_by_state(check_operation_list)}")
print(f"Отмененные: {processing.filter_by_state(check_operation_list, state='CANCELED')}")

print(f"Отсортированный по дате список операций:\n {processing.sort_by_date(check_operation_list)}")
print(f"В обратном порядке:\n {processing.sort_by_date(check_operation_list, is_reverse_order=False)}")
