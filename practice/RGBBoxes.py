r, g, b, n = map(int, input().split())
ans = 0
for i in range(0, n+1, r):
    for j in range(0, n+1, g):
        if not (n-i-j) % b and n-i-j >= 0:
            ans += 1
print(ans)
