import collections
n = int(input())
a = list(map(int, input().split()))
ans = [0, 0]
l = dict(collections.Counter(a))
for i, j in l.items():
    if j >= 2:
        ans.append(i)
    elif j >= 4:
        ans.append(i)
ans.sort()
print(ans[-1]*ans[-2])
