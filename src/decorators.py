import datetime
from functools import wraps
from typing import Any, Callable


def write_log(filename: str | None, log_message: str) -> None:
    if filename:
        with open(filename, "a") as f:
            f.write(log_message)
    else:
        print(log_message.strip())


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования выполнения функций"""

    def decorator(func: Callable) -> Any:
        """Внутренний декоратор, применяемый к функции"""

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            """Обертка, выполняющая логирование"""
            # Формируем строку с информацией о вызове
            func_name = func.__name__
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Формируем сообщение об успехе
                log_message = f"{timestamp} - {func_name} ok\n"

                write_log(filename, log_message)

                return result

            except Exception as e:
                # Формируем сообщение об ошибке
                error_type = type(e).__name__
                inputs = f"Inputs: {args}, {kwargs}"
                log_message = f"{timestamp} - {func_name} error: {error_type}. {inputs}\n"

                write_log(filename, log_message)
                raise

        return wrapper

    return decorator
