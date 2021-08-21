# CS1010S AY20/21 Sem 1 Finals
def wow(n):
    print(n)
    return lambda m: n + m

def twice(t):
    print('yes')
    return lambda x: t(t(x))

once = twice(twice)(wow(2))
print(once(1))