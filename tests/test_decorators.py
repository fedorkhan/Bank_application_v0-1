from src.decorators import log


def test_log_1():
    @log()
    def simple_string():
        return "This is a string"

    assert simple_string() == "This is a string"


def test_log_print(capsys):
    @log()
    def simple_string():
        return "This is a string"

    simple_string()
    captured = capsys.readouterr()
    output = captured.out.split("\n")

    assert output[0] == "Имя функции: simple_string"
    assert output[1][:24:] == "Начало работы программы:"
    assert output[2] == "Успешно. Результат работы функции: This is a string"
    assert output[3][:23:] == "Конец работы программы:"


def test_log_err(capsys):
    @log()
    def error_raiser(arg=0):
        raise TypeError

    error_raiser(1)
    captured = capsys.readouterr()
    output = captured.out.split("\n")

    assert output[0] == "Имя функции: error_raiser"
    assert output[1][:24:] == "Начало работы программы:"
    assert output[2] == "Ошибка: <class 'TypeError'>."
    assert output[3] == "Аргументы, переданные функции: (1,), {}"
    assert output[4][:23:] == "Конец работы программы:"


def test_log_file():
    @log("output.txt")
    def simple_string():
        return "This is a string"

    simple_string()

    with open("output.txt", "r", encoding="utf-8") as file1:
        output = file1.readlines()

    assert output[0] == "Имя функции: simple_string\n"
    assert output[1][:24:] == "Начало работы программы:"
    assert output[2] == "Успешно. Результат работы функции: This is a string\n"
    assert output[3][:23:] == "Конец работы программы:"
