n = int(input())
a = sorted(list(map(int, input().split())))
ans = a[0]
for i in range(1, n):
    cnt = sum(a[:i])
    if cnt < a[i]:
        ans = min(a[i]-cnt, ans)
print(ans)
