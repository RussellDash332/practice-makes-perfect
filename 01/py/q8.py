def iterate(x):
    total = 0
    for i in range(x):
        if x % 2 == 1:
            total += i
    return total