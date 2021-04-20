n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in a:
    if i not in b:
        ans.append(i)
for i in b:
    if i not in a:
        ans.append(i)
print(*sorted(ans))
