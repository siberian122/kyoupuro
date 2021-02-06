v, t, s, d = map(int, input().split())
n = d/v
if t <= n <= s:
    print("No")
else:
    print("Yes")
