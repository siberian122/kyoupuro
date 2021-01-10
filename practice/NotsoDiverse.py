n, k = map(int, input().split())
a = list(map(int, input().split()))
d = [0 for _ in range(n)]
for i in a:
    d[i-1] += 1
d.sort(reverse=True)
cnt = 0
for i in range(k):
    cnt += d[i]
print(n-cnt)
