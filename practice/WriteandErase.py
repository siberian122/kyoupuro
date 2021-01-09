n = int(input())
d = {}
for i in range(n):
    a = input()
    if not a in d:
        d[a] = 1
    else:
        d[a] += 1
ans = 0
for i, j in d.items():
    if j % 2:
        ans += 1
print(ans)
