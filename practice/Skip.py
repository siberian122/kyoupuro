import math
n, x = map(int, input().split())
l = list(map(int, input().split()))
l = [abs(x-i) for i in l]
ans = l[0]
for i in range(1, n):
    ans = math.gcd(ans, l[i])
print(ans)
