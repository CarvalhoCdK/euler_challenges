def sum_multiples(limit):
    multiples = [y for y in range(limit) if (y % 3 == 0) or (y % 5 == 0)]
    print(sum(multiples))


sum_multiples(10000)
