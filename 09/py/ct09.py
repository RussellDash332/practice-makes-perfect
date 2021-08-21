# CS1010X AY16/17 Special Term I Finals
a = {(1, 2): 3, (3, 4): 5}
for k, v in a.items():
    a[[v, k[0]]] = k[1]
b = list(a.values())
b.sort(reverse = True)
print(b)