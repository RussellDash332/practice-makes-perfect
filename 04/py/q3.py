def compose(f, g):
    return lambda x: f(g(x))

def thrice(f):
    return compose(compose(f, f), f)

print(thrice(thrice)(lambda x: x-1)(27))