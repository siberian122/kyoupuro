import collections
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0
a = collections.Counter(a)
cnt = k
for i in range(n):
    if a[i] < cnt:
        cnt = a[i]
    ans += cnt
print(ans)
