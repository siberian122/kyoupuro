n = int(input())
a = list(map(int, input().split()))
ans = float('inf')
l = sum(a)

for i in range(n-1):
    ans = min(ans, abs(l-2*a[i]))
print(ans)
