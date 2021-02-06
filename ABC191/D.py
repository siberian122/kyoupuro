x, y, r = map(float, input().split())
ans = 0
"""
print(int(x-r), int(x+r))
print(int(y-r), int(y+r))
"""
for i in range(int(x-r), int(x+r)+1):
    for j in range(int(y-r), int(y+r)+1):
        z = (i-x)*(i-x)+(j-y)*(j-y)
        if z <= r:
            ans += 1
print(ans)
