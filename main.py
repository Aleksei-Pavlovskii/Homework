from src.decorators import log


@log()
def sum_numbers(a: int, b: int) -> int:
    return a + b


print(sum_numbers(2, 4))
