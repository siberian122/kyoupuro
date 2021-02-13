n, k, s = map(int, input().split())
a = []
for _ in range(k):
    a.append(s)
for _ in range(n-k):
    if s == 10**9:
        a.append(s-1)
    else:
        a.append(s+1)
print(*a)
