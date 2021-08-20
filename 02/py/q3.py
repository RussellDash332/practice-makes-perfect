a, b, c = "east", "easter", "easy"
a, b, c = c, a, b

if a < b:
    a, b = b, a
else:
    if b < c:
        a += b
b = a + c

print(a[:-1])
print(b[1:])
print(c[::-1])