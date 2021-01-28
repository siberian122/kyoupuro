import math
a, b, c, d = map(int, input().split())


def count(n, c, d):
    l = c * d // math.gcd(c, d)
    nc = n//c
    nd = n//d
    ncd = n//l
    return n-(nc+nd-ncd)


cntA = count(a-1, c, d)
cntB = count(b, c, d)
print(cntB-cntA)
print(cntA)
