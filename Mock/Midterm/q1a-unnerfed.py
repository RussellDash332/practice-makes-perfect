x, y = 3, 12
def f(x, y):
    x += y
    y %= x
    return x * y
z, y = f(y, x), 1
print(f(y, z - x))
