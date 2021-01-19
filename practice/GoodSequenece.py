import collections
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i, j in collections.Counter(a).items():
    if i > j:
        ans += j
    elif j > i:
        ans += j-i
print(ans)
