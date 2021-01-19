n = int(input())
a = list(map(int, input().split()))
m = max(a)
dp = [0 for _ in range(m+1)]
for i in a:
    if dp[i] != 0:
        dp[i] = 2
        continue
    num = i
    for _ in range(m):
        if num > m:
            break
        dp[i] += 1
        num += i
# print(dp)
ans = 0
for i in a:
    if dp[i] == 1:
        ans += 1
print(ans)
