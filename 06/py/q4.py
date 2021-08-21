a = [1, 2]
a += [a]
print(a)
b = a.copy() # shallow copy vs deep copy
a[2] = 0
print(a)
print(b)