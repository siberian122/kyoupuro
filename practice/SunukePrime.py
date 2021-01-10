n, C = map(int, input().split())
data = []
for _ in range(n):
    a, b, c = map(int, input().split())
    data.append((a-1, c))
    data.append((b, -c))

data.sort()
ans = 0
fee = 0
t = 0
for i, l in data:
    if i != t:
        ans += min(C, fee) * (i-t)
        t = i
    fee += l
print(ans)
