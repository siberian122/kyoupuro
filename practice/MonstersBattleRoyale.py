import math
n = int(input())
a = sorted(list(map(int, input().split())))
ans = a[0]
for i in range(1, n):
    A = a[i]
    ans = math.gcd(A, ans)
print(ans)
