x, y = 1, 4
x, y = y, x

def ding(x):
    if x % 2 == 1:
        print("Alright")
    elif x % 3 == 1:
        print("Okay")
    if x**0.5 == y + 1:
        print("Awesome")
    else:
        print("This question sucks")

ding(x)
ding(y)
ding(9)
print(ding(3))  # what happens here?