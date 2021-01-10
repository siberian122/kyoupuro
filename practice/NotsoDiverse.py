n, k = map(int, input().split())
a = list(map(int, input().split()))
d = {}

for i in a:
    if not i in d:
        d[i] = 1
    else:
        d[i] += 1
ans = 0
while len(d) > k:
    num = min(d)
    ans += d[num]
    d = d.pop(num)
print(ans)
