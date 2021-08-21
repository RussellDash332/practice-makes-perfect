# CS1010S AY17/18 Sem 2 Finals
def foo(x):
    return lambda y: bar(x) if y % 2 else x
def bar(y):
    return lambda x: foo(x) if y % 2 else y

print(foo(2)(3)(4))