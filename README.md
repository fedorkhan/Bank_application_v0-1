# Виджет банковского приложения

## Описание

Виджет банковского приложения - это backend-часть приложения на Python для отображения различной информации клиенту банка
Проект реализуется в рамках заданий по курсу *Python-разаработчик*

## Установка

1. Работа с виртуальным окружением производится при помощи менеджера пакетов Poetry
Перед началаом установки самого приложения убедитесь, что у вас утсановлен и подключен Poetry
2. Клонируйте репозиторий ` https://github.com/fedorkhan/Bank_application_v0-1.git `

## Примеры использования функций

```
from src import generators, processing, widget


print(widget.get_date("2024-03-11T02:26:18.671407"))

#Примеры работы с функцией маскировки:
print(widget.mask_account_card("Счет 64686473678894779589"))
print(widget.mask_account_card("Visa Gold 5999414228426353"))

print(widget.mask_account_card("Maestro 1596837868705199"))

#генерация номеров карт в диапазоне от start=12378568569997 до stop=12378568569999:
print(list(generators.card_number_generator(12378568569997, 12378568569999)))

#Фильтр по валюте операций из списка транзакций 'transactions' по доллару 'USD' и рублю 'RUB'
print(list(generators.filter_by_currency(transactions, "USD")))
print(list(generators.filter_by_currency(transactions, "RUB")))

#вывод деталей по операциям из списка транзакций 'transactions'
obtained_descriptions = generators.transaction_descriptions(transactions)
for index in range(len(transactions)):
    print(next(obtained_descriptions))

#Вывод отмененных операций:
print(f"Отмененные: {processing.filter_by_state(check_operation_list, state='CANCELED')}")
#Сортировка операций в обратном порядке
print(f"В обратном порядке:\n {processing.sort_by_date(check_operation_list, is_reverse_order=False)}")

```
## Тестирование
Тестирование проводилось при помощи фреймворка `pytest`.

Степень покрытия кода тестами оценивалась при помощи библиотеки `pytest-coverage`. 
Тесты находятся в папке `/tests/test_generators.py`, а результаты покрытия тестами кода -- в `/htmlcov/index.html`


## Результаты тестирования
Тестирование модулей программы проводилось при помощи фреймворка *pytest*.

Примеры тестов находятся в пакете ` /tests/ `. 

Результаты по оценке покрытия кода тестами в формате `.html` находятся в `/htmlcov/index.html`

## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).
