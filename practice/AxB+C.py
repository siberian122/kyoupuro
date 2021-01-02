n = int(input())
ans = 0
for i in range(n):
    ans += (n-1)//i
print(ans)
