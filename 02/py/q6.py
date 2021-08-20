def weird_sum(n):
    if n == 0:
        return 0 
    else:
        return n + weird_sum(n - 2)

print(weird_sum(5))