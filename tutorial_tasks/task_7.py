from typing import Callable


def smart_divide(func: Callable[[int, int], float]):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


print(divide(9, 1))
