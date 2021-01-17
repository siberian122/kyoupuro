n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7
num = sum(a)
ans = 0
for i in range(n-1):
    num -= a[i]
    ans += a[i] * num


print(ans % mod)
