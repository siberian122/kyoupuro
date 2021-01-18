n = int(input())
a = list(map(int, input().split()))
cumsum = 1
for i in a:
    cumsum *= i
ans = 0
for i in a:
    if (cumsum//i) % i >= 1:
        ans += 1
print(ans)
