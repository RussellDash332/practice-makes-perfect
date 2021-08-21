def foo(x):
    def bar(x, y):
        return lambda y: y(x)
    return lambda y: bar(x, y)

print(foo(lambda x: x**3)(lambda x: x**2)(lambda x: x)(4))