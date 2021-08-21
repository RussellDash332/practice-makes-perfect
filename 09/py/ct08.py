# CS1010FC AY14/15 Special Term I Finals
a = {1: 2, 2: 4, 3: 6, 4: 7}
for k in a:
    if k % 2 == 1:
        del a[k]
print(a)