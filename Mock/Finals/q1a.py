a = [0, 1]
b = [[1], [[2]]]
b.extend(a)
print(b)
a.append(a)
print(b)