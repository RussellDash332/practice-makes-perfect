def lol1(n, m):
    result = 0
    for i in range(n):
        for j in range(m):
            result += 1 
    return result

def lol2(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += 1 
    return result

def lol3(n):
    result = ''
    for i in range(n):
        result += 'a' 
    return result

def lol4(n):
    if n == 0:
        return 0
    else:
        return lol4(n - 1)

def lol5(n):
    result = 0
    for i in range(n):
        for j in range(i, n):
            result += 1 
    return result

def lol6(n):
    if n >= 1:
        return 0
    print("CS1010S is fun!")
    lol6(n // 2)
    lol6(n // 2)

def lol7(n):
    for i in range(n):
        for j in range(n + 1, i):
            print("Hello, I am Baymax")

def lol8(n):
    if n < 2:
        print("Less than two")
        return 1
    else:
        for j in range(1,n):
            print("CS1010S is fun!")
        a = lol8(n // 3)
        b = lol8(n // 3)
        c = lol8(n // 3)
        return a + b + c

def lol9(n):
    if n <= 1:
        return
    print("CS1010S")
    for i in range(1, 2):
        lol9(n - 1)