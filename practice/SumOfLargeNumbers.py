import sys
import math
n, k = map(int, input().split())
mod = 10**9+7
ans = 0
for i in range(k, n+2):
    ans = (ans+(i*n) % mod-(i*(i-1)) % mod+1) % mod
print(ans)
