result = 0
for i in range(1, 13, 3):
    if i % 2 == 0:
        i += 2
    else:
        result //= i
    result += i

print(result)