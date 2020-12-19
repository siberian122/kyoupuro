t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    ans = -1

    if (n-s) % k == 0:
        ans = (n-s)//k
    print(ans)
