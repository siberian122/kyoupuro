n = int(input())
ans = 0
for i in range(1, n+1):
    x = n//i
    ans += (x+1)*x*i//2
print(ans)
