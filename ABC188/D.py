n, C = map(int, input().split())
data = [0 for i in range(10**9)]
mb = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    data[a] += c
    data[b] -= c
    mb = max(b, mb)
ruiseki = [0 for _ in range(mb+1)]
ruiseki[0] = data[0]

for i in range(1, mb):
    ruiseki[i] = ruiseki[i-1] + data[i]

for i in range(mb):
    if i > C:
        ruiseki[i] = C
print(sum(ruiseki))
