a = []

temp = [0]*4
for i in range(3):
    a.append(temp)

a[1][1] = 99
print(a)