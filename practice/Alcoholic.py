n, x = map(int, input().split())
x *= 100
chk = 0
ans = -1
for i in range(n):
    v, p = map(int, input().split())
    chk += v*p
    if chk > x:
        ans = i+1
        break
print(ans)
