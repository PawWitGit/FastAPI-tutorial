def InfiniteNaturals():
    start = 1
    while start < 100232323232332322:
        yield start
        start += 1


numbers = InfiniteNaturals()
for item in numbers:
    print(item)
