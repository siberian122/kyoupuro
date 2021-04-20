n = int(input())
a = list(map(int, input().split()))
ans = float("inf")
for i in range(2**(n-1)):
    l, k = 0, 0
    for j in range(n):
        l |= a[j]
        if ((i >> j) & 1) or j == n-1:
            k ^= l
            l = 0

    ans = min(ans, k)

print(ans)
