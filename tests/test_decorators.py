import os
import pytest
from decorators import log


# Тестовые функции для проверки
@log()
def console_success(a, b):
    return a + b


@log()
def console_failure():
    raise ValueError("Test error")


@log(filename="test_log.txt")
def file_success(x, y):
    return x * y


@log(filename="test_log.txt")
def file_failure():
    raise TypeError("File error")


def test_console_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""
    assert console_success(2, 3) == 5
    captured = capsys.readouterr()
    assert "console_success started" in captured.out
    assert "console_success ok" in captured.out


def test_console_error(capsys):
    """Тест ошибки с выводом в консоль"""
    with pytest.raises(ValueError):
        console_failure()
    captured = capsys.readouterr()
    assert "console_failure started" in captured.out
    assert "console_failure error: ValueError" in captured.out
    assert "Inputs: (), {}" in captured.out


def test_file_success():
    """Тест успешного выполнения с записью в файл"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    assert file_success(3, 4) == 12

    with open("test_log.txt", "r", encoding='utf-8') as f:
        content = f.read()
        assert "file_success started" in content
        assert "file_success ok" in content


def test_file_error():
    """Тест ошибки с записью в файл"""
    with pytest.raises(TypeError):
        file_failure()

    with open("test_log.txt", "r", encoding='utf-8') as f:
        content = f.read()
        assert "file_failure started" in content
        assert "file_failure error: TypeError" in content
        assert "Inputs: (), {}" in content


