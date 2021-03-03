n = int(input())
ans = []
for _ in range(n):
    ans.append(input())
ans = set(ans)
print(len(ans))
