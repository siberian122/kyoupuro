n, k, m = map(int, input().split())
a = list(map(int, input().split()))

M = m*n - sum(a)
ans = -1
for x in range(k + 1):
    if x >= M:
        ans = x
        break
print(ans)
