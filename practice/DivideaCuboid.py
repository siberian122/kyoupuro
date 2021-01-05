a = list(map(int, input().split()))
n = a.index(max(a))
x, y = 1, 1
for i in range(3):
    if i != n:
        x *= a[i]
        y *= a[i]
    else:
        x *= a[i]//2
        y *= a[i]-a[i]//2
print(y-x)
