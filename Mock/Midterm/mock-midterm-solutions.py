# Question 1
"""
1806
"""
##x, y = 3, 12
##def f(x, y):
##    x += y
##    y %= x
##    return x * y
##z, y = f(y, x), 1
##print(f(y, z - x))

"""
(-1, 2, -1, 7, 4, -1)
"""
##p, q = (), (7, 4, 2, 5, 3)
##for r in q:
##    if r % 5 == 2:
##        p = (-1, r,) + p[1:]
##    elif r % 2 == 0:
##        p = (r,) + p + (r, -1)
##print(p)

"""
yum tum
"""
##m, p = "mutton", "python"
##mp = m+p+"ton"
##if "on" in mp:
##    if p in mp:
##        p = "p"
##        print("yum")
##    if "on" in p:
##        print("bum")
##    elif mp:
##        print("tum")

"""
420 280 140 92 46 7.5
"""
##n = 420
##while n >= -1:
##    print(n)
##    n //= 3
##    if n % 2 == 0:
##        print(2*n)
##        continue
##    elif n % 7 == 1:
##        print(n/2)
##        break
##    n //= 2
##    n -= 2

"""
72
"""
##def con(x, y):
##    return lambda z: y(x, z)
##def fuse(x):
##    return lambda y: x(y, y)
##why = lambda x,y: x*y
##so = lambda x,y: x**2 + y
##hard = lambda y,x: 2*x + y
##dif = con(fuse(so)(3), why)
##print(dif(fuse(hard)(2)))



# Question 2
def choose(n, m):
    if n <= 0 or m < 0:
        return 0
    if n == m or m == 0:
        return 1
    return choose(n-1, m-1) + choose(n-1, m)
# Time: actually O(nCm), but for CS1010S we accept any approximations such as O(n^n), O(n^m) and so on
# Space: O(n), again the depth of the tree

def choose_iterative(n, m):
    if n <= 0 or m < 0:
        return 0
    if n == m or m == 0:
        return 1 # not necessary but is fine
    result = 1
    for i in range(m):
        result *= (n-i)/(i+1)
    return int(result)
# Time: O(m)
# Space: O(1)

def cumulative_prob_iterative(n, p, k):
    result = 0
    for i in range(k+1):
        result += choose_iterative(n, i)*(p**i)*((1-p)**(n-i))
    return result
# Assuming choose_iterative is O(m) time
# Time: O(k^2) because for each iteration i of the loop we are doing O(i) operations.
#       Thus the total operations needed is O(1 + 2 + 3 + ... + k) = O(k^2)
# Space: O(1)

def cumulative_prob_recursive(n, p, k):
    if k == 0:
        return choose_iterative(n, 0)*(1-p)**n
    else:
        return cumulative_prob_recursive(n, p, k-1) + choose_iterative(n, k)*(p**k)*((1-p)**(n-k))
# Assuming choose_iterative is O(m) time
# Time: O(k^2)
# Space: O(k)



# Question 3
def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))

def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def choose_hof(n, k):
    return int(fold(lambda x,y: x*y, lambda x: (n-x+1)/x if x != 0 else 1, k))

def cumulative_prob_hof(n, p, k):
    return sum(lambda x: choose_hof(n, x)*(p**x)*((1-p)**(n-x)), 0, lambda x: x+1, k)



# Question 4
def make_account():
    return (1000, ())

def add_coins(account, amt):
    return (account[0] + amt, account[1])

def obtain_powerpoint(account, brawler, points):
    result = (account[0] - 2*points,)
    brawlers = ()
    exist = False
    for i in account[1]:
        if i[0] == brawler:
            exist = True
            brawlers += ((i[0], i[1]+points),)
        else:
            brawlers += (i,)

    if not exist:
        brawlers += ((brawler, points),)

    return result + (brawlers,)
            

def get_coins(account):
    return account[0]

def get_brawlers(account):
    result = ()
    for i in account[1]:
        result += (i[0],)
    return result

def get_level(account, brawler):
    def level(p):
        if p == 0:
            return 0
        elif 1 <= p <= 19:
            return 1
        elif 20 <= p <= 49:
            return 2
        elif 50 <= p <= 99:
            return 3
        elif 100 <= p <= 199:
            return 4
        elif 200 <= p <= 549:
            return 5
        return 6

    for i in account[1]:
        if i[0] == brawler:
            return level(i[1])
    return 0

def obtain_powerpoint_better(account, brawler, points):
    balance = account[0] - 2*points
    brawlers = ()
    exist = False
    for i in account[1]:
        if i[0] == brawler:
            exist = True
            # There might be a simpler solution but this works
            excess = max(550, i[1]+points)-550
            brawlers += ((i[0], min(550, i[1]+points)),)
            balance += 2*excess
        else:
            brawlers += (i,)

    if not exist:
        brawlers += ((brawler, points),)

    return (balance, brawlers)
