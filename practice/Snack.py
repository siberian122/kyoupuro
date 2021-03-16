import math
a, b = map(int, input().split())


def lcm(x, y):
    return int(a*b/math.gcd(x, y))


print(lcm(a, b))
