p, q = (), (7, 4, 2, 5, 3)
for r in q:
    if r % 5 == 2:
        p = (-1, r,) + p[1:]
    elif r % 2 == 0:
        p = (r,) + p + (r, -1)
print(p)
