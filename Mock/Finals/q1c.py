kh, z = "kenghwee", "zoink"
sus = 0
for s in kh:
    if s in z:
        sus += 1
    if s == "e":
        print(sus)
    elif s > "k":
        sus *= 2
print(sus)