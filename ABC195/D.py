n, m, q = map(int, input().split())
nimotu = [list(map(int, input().split())) for _ in range(n)]
nimotu = sorted(nimotu, reverse=True, key=lambda x: x[1])
# print(nimotu)
x = list(map(int, input().split()))
for _ in range(q):
    ans = 0
    l, r = map(int, input().split())
    box = sorted(x[:l-1]+x[r:])
    ined = []

    for j in box:
        for i in range(n):
            if j >= nimotu[i][0] and i not in ined:
                ans += nimotu[i][1]
                ined.append(i)
                break
    print(ans)
