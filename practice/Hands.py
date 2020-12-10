a, b, x, y = map(int, input().split())
ans = 0
if a == b:
    if x < y:
        ans = x
    else:
        ans = y
elif a < b:
    if 2*x <= y:
        cnt = 2 * x
    else:
        cnt = y
    for i in range(b-a):
        ans += cnt
    ans += x
elif a-1 == b:
    if x < y:
        cnt = x
    else:
        cnt = y
    ans = cnt
else:
    if 2*x < y:
        cnt = 2*x
    else:
        cnt = y
    for i in range(a-b):
        ans += cnt
    ans += x
print(ans)
