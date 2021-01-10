import numpy as np
n, C = map(int, input().split())
data = np.array([0 for i in range(10**9)])
mb = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    data[a] += c
    data[b+1] -= c
    mb = max(b, mb)
ruiseki = [0 for _ in range(mb+2)]
ruiseki[0] = data[0]

for i in range(1, mb+2):
    ruiseki[i] = ruiseki[i-1] + data[i]

for i in range(mb+2):
    if ruiseki[i] > C:
        ruiseki[i] = C
# print(ruiseki)
print(sum(ruiseki))
