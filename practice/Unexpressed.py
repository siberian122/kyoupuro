n = int(input())
N = int(n**0.5)
ans = []
for i in range(2, N+1):
    num = i * i
    while num <= n:
        ans.append(num)
        num *= i
ans = set(ans)
print(n-len(ans))
