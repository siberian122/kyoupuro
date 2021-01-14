n = int(input())
h = list(map(int, input().split()))
N = max(h)
ans = 0
for i in range(1, N+1):
    ok = False
    cnt = 0
    for l in h:
        if ok and l < i:
            ok = False
        elif not ok and l >= i:
            ok = True

            cnt += 1
    ans += cnt
    # print(cnt)

print(ans)
