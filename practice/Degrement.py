n = int(input())
p = list(map(int, input().split()))
ans = 0
while True:
    cnt = 0
    for i in range(n-1):
        if i+1 == p[i]:
            p[i], p[i+1] = p[i+1], p[i]
            ans += 1
            continue
        else:
            cnt += 1
    if cnt == n-1:
        break
print(ans)
