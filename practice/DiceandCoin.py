n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    if i >= k:
        ans += 1/n
    else:
        num = i
        cnt = 0
        while num < k:
            num *= 2
            cnt += 1
        # print(cnt)
        ans += (1/n) * (1/2) ** cnt
print(ans)
