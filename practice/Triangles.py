import bisect
n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += bisect.bisect_left(l, l[i]+l[j])-j-1
        print(ans)
print(ans)
