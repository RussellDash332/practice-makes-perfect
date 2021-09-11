n = 420
while n >= -1:
    print(n)
    n //= 3
    if n % 2 == 0:
        print(2*n)
        continue
    elif n % 7 == 1:
        print(n/2)
        break
    n //= 2
    n -= 2
