import datetime


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Формируем строку с информацией о вызове
            func_name = func.__name__
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Формируем сообщение об успехе
                log_message = f"{timestamp} - {func_name} ok\n"

                # Логируем результат
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())

                return result

            except Exception as e:
                # Формируем сообщение об ошибке
                error_type = type(e).__name__
                inputs = f"Inputs: {args}, {kwargs}"
                log_message = f"{timestamp} - {func_name} error: {error_type}. {inputs}\n"

                # Логируем ошибку
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())

                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
