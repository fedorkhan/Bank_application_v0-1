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
from src import widget

print(widget.get_date("2024-03-11T02:26:18.671407"))

#Примеры работы с функцией маскировки:
print(widget.mask_account_card("Счет 64686473678894779589"))
print(widget.mask_account_card("Visa Gold 5999414228426353"))

#Вывод отмененных операций:
print(f"Отмененные: {processing.filter_by_state(check_operation_list, state='CANCELED')}")
#Сортировка операций в обратном порядке
print(f"В обратном порядке:\n {processing.sort_by_date(check_operation_list, is_reverse_order=False)}")
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).
