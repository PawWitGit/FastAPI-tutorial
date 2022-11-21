price = [210, 300, 400, 500]

price_iter = price.__iter__()

for i in range(len(price)):
    print(price_iter.__next__())
