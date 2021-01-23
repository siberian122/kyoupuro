n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    cnt = a[i]
    for j in range(i, n):
        cnt = min(cnt, a[j])
        ans = max(ans, (cnt*(j-i+1)))
print(ans)
