n, m, t = map(int, input().split())

ans = 'Yes'
now = n
s = 0
for _ in range(m):
    a, b = map(int, input().split())
    now = now - (a-s)
    # print(now)
    if now <= 0:
        ans = 'No'
    if (now + b-a) <= n:
        now += b-a
    else:
        now = n

    s = b
if now - (t-s) <= 0:
    ans = 'No'
print(ans)
