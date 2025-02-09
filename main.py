from src import processing, widget

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

print(f"Успешные: {processing.filter_by_state(check_operation_list)}")
print(f"Отмененные: {processing.filter_by_state(check_operation_list, state='CANCELED')}")

print(f"Отсортированный по дате список операций:\n {processing.sort_by_date(check_operation_list)}")
print(f"В обратном порядке:\n {processing.sort_by_date(check_operation_list, is_reverse_order=False)}")
