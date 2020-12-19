
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
for i in range(n):
    ans -= a[i]*i
    ans += a[i]*(n-1-i)
print(ans)
