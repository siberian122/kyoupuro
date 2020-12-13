import math


def comb(n, r):
    return math.factorial(n)//math.factorial(n-r)


def func(n):
    res = 0
    for i in range(1, n+1):
        res += comb(12, i)
    return res


l = int(input())


num = l % 12

ans = 0
for i in range(1, num+1):
    ans += func(i)


print(ans)
