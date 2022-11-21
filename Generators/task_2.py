from typing import Any, Iterator


class NaturalNumbers:

    """Infinite iterator"""

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


value = iter(NaturalNumbers())
for i in range(5):
    print(next(value))
