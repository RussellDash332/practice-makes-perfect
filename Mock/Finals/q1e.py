def bar(z):
    return lambda r: baz(r - 1) \
            if r > 5 else r + z
def baz(r):
    return lambda z: bar(z // 2) \
            if z > 0 else 5
print(baz(4)(100)(4))