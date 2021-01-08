n = int(input())

s = [int(input()) for _ in range(n)]
s.sort()
ans = sum(s)
if not ans % 10:
    for i in s:
        if i % 10:
            ans -= i
            break
if not ans % 10:
    ans = 0
print(ans)
