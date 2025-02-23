from functools import wraps
from time import time


def log(filename=None):
    """
        Автоматически логирует начало и конец выполнения функции,
        а также ее результаты или возникшие ошибки.
        Выводит эти данные либо в файл, заданный необязательным параметром 'filename',
        либо в консоль, если параметр filename не задан
    """
    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):

            def logger(log_data_list1, filename1):
                log_data = "\n".join(log_data_list1)

                if filename1 is None:
                    print(log_data)
                else:
                    try:
                        file1 = open(filename1, "w", encoding="utf-8")
                        file1.write(log_data)
                    except PermissionError:
                        print(f"Cannot write data to {filename1}!")

            log_data_list = []

            name_ = function.__name__
            log_data_list.append(f"Имя функции: {name_}")

            start_time = time()
            log_data_list.append(f"Начало работы программы: {start_time}")

            try:
                result = function(*args, **kwargs)
                stop_time = time()
                log_data_list.append(f"Успешно. Результат работы функции: {result}")
                log_data_list.append(f"Конец работы программы: {stop_time}")
                log_data_list.append("\n")
                logger(log_data_list, filename)
                return result

            except Exception as e_msg:
                error_message = (f"Ошибка: {type(e_msg)}.\n"
                                 f"Аргументы, переданные функции: {args}, {kwargs}")
                stop_time = time()
                log_data_list.append(error_message)
                log_data_list.append(f"Конец работы программы: {stop_time}")
                log_data_list.append("\n")
                logger(log_data_list, filename)

        return inner

    return wrapper
