n = int(input())
d = {}
for i in range(n):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
m = int(input())
for i in range(m):
    s = input()
    if s not in d:
        d[s] = -1
    else:
        d[s] -= 1
ans = max(d.values())
if ans > 0:
    print(max(d.values()))
else:
    print(0)
