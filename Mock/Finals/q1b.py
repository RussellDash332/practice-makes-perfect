d, msp = {}, "mississippi"
for x in msp:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
        d[d[x]] = 1
print(d)