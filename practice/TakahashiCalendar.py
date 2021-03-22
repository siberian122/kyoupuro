m, d = map(int, input().split())
ans = 0
for i in range(4, m+1):
    for j in range(22, d+1):
        j = str(j)
        d0 = int(j[0])
        d10 = int(j[1])
        if d0 * d10 == i and d0 > 1 and d10 > 1:
            ans += 1
print(ans)
