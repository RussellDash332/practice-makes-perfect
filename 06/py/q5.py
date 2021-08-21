a = [1, 2, 3]
b = [4, a]
c = [a, b, 15, b[0], b[1]]

c[1][0] = 99
print(b)
print(c)

c[3] = 100
print(b)
print(c)

a[1] = 200
print(a)
print(b)
print(c)

b[1][2] = 300
print(a)
print(b)
print(c)

d = [4, c.copy()]
c[2] = 500
c[0][2] = 500
print(d)