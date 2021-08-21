# CS1010S AY19/20 Sem 2 Finals
lst = [[1], [2, 2], [3, 3, 3]]

def f(lst):
    for i in lst.copy():
        if len(i) < 2:
            i.append(1)
        if sum(i) < 5:
            i.pop()
        else:
            lst.extend(i)
        print(lst)
    return lst

print(lst is f(lst))
print(lst)