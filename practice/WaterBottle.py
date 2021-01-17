import math

a, b, x = map(int, input().split())
cap = a*a*b
if cap/2 < x:  # 半分より多い
    print(math.degrees(math.atan(2*b/a - 2*x/a/a/a)))
else:  # 半分以下
    print(math.degrees(math.atan(a*b*b/2/x)))
