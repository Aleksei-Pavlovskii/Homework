import pytest

from src.decorators import log


# Тестовые функции для проверки
@log()
def console_success(a, b):
    return a + b


@log()
def console_failure():
    raise ValueError("Test error")


@log(filename="logs/test_log.txt")
def file_success(x, y):
    return x * y


@log(filename="test_log.txt")
def file_failure():
    raise TypeError("File error")


def test_console_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""
    assert console_success(2, 3) == 5
    captured = capsys.readouterr()
    assert "console_success ok" in captured.out


def test_console_error(capsys):
    """Тест ошибки с выводом в консоль"""
    with pytest.raises(ValueError):
        console_failure()
    captured = capsys.readouterr()
    assert "console_failure error: ValueError" in captured.out
    assert "Inputs: (), {}" in captured.out


def test_write_log():
    file_success(1, 2)
    assert "file_success ok\n" in open("logs/test_log.txt", encoding="utf-8").read()
