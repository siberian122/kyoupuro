import math

a, b, x = map(int, input().split())
cap = a*a*b
if cap/2 < x:
    print(math.degrees(math.atan(2*b/a - 2*x/a/a/a)))
else:
    print(math.degrees(math.atan(a*b*b/2/x)))
