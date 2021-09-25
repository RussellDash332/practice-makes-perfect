def p(p, q):
    print(p)
    return q(p + q(p))
def q(q):
    print(q)
    return q + q
print(p(2, q))