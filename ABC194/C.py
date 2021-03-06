import itertools
n = int(input())
a = list(map(int, input().split()))
ans = 0
l = itertools.combinations(a, 2)


for i, j in l:
    ans += abs(i-j) ** 2
print(ans)
