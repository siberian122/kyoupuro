s = input()
R = ["R", "U", "D"]
L = ["L", "U", "D"]
ans = "Yes"
for i in range(len(s)):
    if i % 2:
        if s[i] not in L:
            ans = "No"
            break
    else:
        if s[i] not in R:
            ans = "No"
            break
print(ans)
