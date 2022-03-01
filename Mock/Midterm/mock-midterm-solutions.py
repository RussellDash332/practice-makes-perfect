# Question 1
"""
(Unnerfed)
1A: 1806
1B: (-1, 2, -1, 7, 4, -1)
1C: yum tum
1D: 420 280 140 92 46 7.5
1E: 72

(Nerfed)
1A: -27
1B: (2, 7, 2, 3, 1)
1C: hum bum
1D: 280 92 7
1E: 34
"""


# Question 2
def choose(n, m):
    if n <= 0 or m < 0:
        return 0
    if n == m or m == 0:
        return 1
    return choose(n-1, m-1) + choose(n-1, m)
# Time: actually O(nCm), but O(2^n) should be okay despite being a weaker bound.
# Most common should be O(2^n), due to the tree drawn as shown
##                            n, k
##                n-1, k-1               n-1, k
##        n-2, k-2      n-2, k-1  n-2, k-1    n-2, k
##      ...     ...   ...   ... ...     ...  ...   ...
# Note that each level decreases n by 1, so the depth of the tree is O(n) and thus
# the complexity is the number of nodes which is O(1 + 2 + ... + 2^n = 2^(n+1)) = O(2^n)
# But actually, there are nCm nodes to be exact.
#
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
# Assuming we use choose_iterative(n, m) which is O(m) time
# Time: O(k^2) because for each iteration i of the loop we are doing O(i) operations.
#       Thus the total operations needed is O(1 + 2 + 3 + ... + k) = O(k^2)
# Space: O(1)

def cumulative_prob_recursive(n, p, k):
    if k == 0:
        return choose_iterative(n, 0)*(1-p)**n
    else:
        return cumulative_prob_recursive(n, p, k-1) + choose_iterative(n, k)*(p**k)*((1-p)**(n-k))
# Assuming we use choose_iterative(n, m) which is O(m) time
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

# The master plan is to use this data structure:
# (coins, ((b1, p1), (b2, p2), (b3, p3), ...))
# Other formats like below are also welcome.
# (coins, (b1, p1), (b2, p2), (b3, p3), ...)

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
        excess = max(550, points)-550
        brawlers += ((brawler, min(550, points)),)
        balance += 2*excess

    return (balance, brawlers)
