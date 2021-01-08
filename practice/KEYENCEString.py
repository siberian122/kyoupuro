s = input()
k = "keyence"
ans = "NO"
for i in range(7):
    if s[:i]+s[len(s)-len(k[i:]):] == k:
        ans = "YES"
print(ans)
