def con(x, y):
    return lambda z: y(x, z)
def fuse(x):
    return lambda y: x(y, y)
why = lambda x,y: x*y
so = lambda x,y: x**2 + y
hard = lambda y,x: 2*x + y
dif = con(fuse(so)(3), why)
print(dif(fuse(hard)(2)))
