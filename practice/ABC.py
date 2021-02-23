import math
k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, math.ceil(k/a)+1):
        ans += math.floor(k/(a*b))
print(ans)
