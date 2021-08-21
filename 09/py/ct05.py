# CS1010S AY19/20 Sem 1 Finals
def foo(x):
    def baz(y):
        return lambda z: (x, y)[z]
    return lambda x: baz(x)

print(foo(-1)(0)(1))