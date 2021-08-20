x = 10
def ping(x):
    return pong(x + 4)
def pong(x):
    x += 1
    return x**2
  
print(ping(3))
print(pong(x))
ping(2) # what happens here?