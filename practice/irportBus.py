n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
limit = t[0] + k
num = 1
ans = 1
for i in range(1, n):
    if num < c and limit >= t[i]:
        num += 1
    else:
        num = 1
        ans += 1
        limit = t[i] + k
print(ans)
