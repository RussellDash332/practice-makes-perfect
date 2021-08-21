# CS1010S AY17/18 Sem 2 Finals
def force(x):
    try:
        return int(x)
    except ValueError:
        return float(x)
    except Exception:
        return "NaN"

print(force("100"))
print(force("1.0"))
print(force("abc"))