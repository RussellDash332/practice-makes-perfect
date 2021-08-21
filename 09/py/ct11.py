# CS1010S AY19/20 Sem 1 Midterm
def foo(x):
    return x(lambda a: a + 1)
def kung(x):
    return foo(lambda a: a(x))
print(kung(foo)(9000))