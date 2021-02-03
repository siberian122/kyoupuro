from collections import Counter
n = int(input())
d = Counter(list(map(int, input().split())))
m = int(input())
t = Counter(list(map(int, input().split())))
ans = "YES"
# print(t)
for i in t:
    if not t[i] <= d[i]:
        ans = "NO"
        break
print(ans)
