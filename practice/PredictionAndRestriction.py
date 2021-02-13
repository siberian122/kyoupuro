n, k = map(int, input().split())
r, s, p = map(int, input().split())
point = {"r": p, "s": r, "p": s}
t = input()
ans = 0
K = ""
for i in t:
    if len(K) < k:
        ans += point[i]
        K += i
    elif K[-k] == i:
        K += "N"  # None
    else:
        ans += point[i]
        K += i
print(ans)
