import collections

n = int(input())
a = list(map(int, input().split()))
tmp = []
for i in range(n):
    tmp.append(i-a[i])
k = collections.Counter(tmp)
# print(k)
cnt = 0
for i in range(n):
    cnt += k[i+a[i]]
print(cnt)
