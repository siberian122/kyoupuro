n = int(input())
a = list(map(int, input().split()))
ans = float('inf')
l = sum(a)
r = 0
for i in range(n-1):
    r += a[i]
    l -= a[i]
    ans = min(ans, abs(r-l))
print(ans)
