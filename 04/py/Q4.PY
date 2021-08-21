foo = lambda y: lambda x: x(y)
add1 = lambda x: x+1

print(foo(add1(2))(foo)(add1))