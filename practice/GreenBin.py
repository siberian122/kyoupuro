import collections
import math
n = int(input())
s = {}


def comb(n, r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))


ans = 0
for _ in range(n):
    ss = str(sorted(input()))
    if ss not in s:
        s[ss] = 1
    else:
        s[ss] += 1
for i in s.values():
    if i > 1:
        ans += int(comb(i, 2))
print(ans)
