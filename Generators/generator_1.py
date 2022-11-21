def return_values():
    yield 1
    yield 2
    yield "a"
    yield "b"


value = return_values()
try:
    for i in range(5):
        print(value.__next__())

except StopIteration:
    print("\nAll was printed!")
