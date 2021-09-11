def con(x):
    return lambda y: y(y(x))
def fuse(x):
    return lambda y: x(x(y))
much = lambda x: x+1
d = lambda x: 4*x
print(con(fuse(d)(2))(much))
