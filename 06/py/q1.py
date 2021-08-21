a = [1, 2, 0, 4, 5, 6]

for i in range(len(a)):
    if a[i] % 2 == 0:
        a.pop(i)
    print(a)