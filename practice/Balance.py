n = int(input())
w = list(map(int, input().split()))
ans = 100 * 100
for i in range(1, n):
    ans = min(ans, abs(sum(w[:i])-sum(w[i:])))
    # print(ans)
print(ans)
