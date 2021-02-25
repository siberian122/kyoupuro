n = int(input())
p = list(map(int, input().split()))
ans = 0
p.append(-1)
for i in range(n):
    if p[i] == i+1:
        p[i+1] = 0
        ans += 1
print(ans)
