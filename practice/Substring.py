s = input()
t = input()
ans = 10000
n = len(t)
for i in range(len(s)-n):
    cnt = 0
    for l in range(n):
        if s[i+l] != t[l]:
            cnt += 1
    ans = min(cnt, ans)
print(ans)
