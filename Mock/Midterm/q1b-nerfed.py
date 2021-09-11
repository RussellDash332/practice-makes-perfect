p, q = (), (7, 4, 2, 5, 3)
for r in q:
    if r % 5 == 2:
        p = (r,) + p
    else:
        p += (r - 2,)
print(p)
