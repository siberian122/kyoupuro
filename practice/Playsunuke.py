n = int(input())
ans = []
for _ in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        ans.append(p)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
