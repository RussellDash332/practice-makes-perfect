# CS1010S AY17/18 Sem 1 Finals
s = 'Lollapalooza'
d = {}
for i in range(len(s)):
    d[s[i % 5]] = s[i]
print(d)