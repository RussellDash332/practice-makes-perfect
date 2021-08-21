# CS1010S AY17/18 Sem 2 Midterm
def foo(y):
    return lambda x: x(x(y))
def bar(x):
    return lambda y: x(y)
print((bar)(bar)(foo)(2)(lambda x: x + 1))