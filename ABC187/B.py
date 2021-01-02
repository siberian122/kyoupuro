import itertools
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n-1):
    x, y = l[i][0], l[i][1]
    for j in range(i+1, n):
        xx, yy = l[j][0], l[j][1]

        if abs((yy-y)/(xx-x)) <= 1:
            ans += 1
print(ans)
