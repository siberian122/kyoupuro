s = input()
ans = 100
for i in set(s):
    cnt = 0
    for j in s.split(i):
        cnt = max(cnt, len(j))
    ans = min(cnt, ans)
print(ans)
