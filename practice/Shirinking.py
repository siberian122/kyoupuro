s = input()
mincnt = 101
for i in range(26):
    c = chr(ord("a") + i)
    cnt = 0
    maxcnt = 0
    for j in range(len(s)):
        if s[j] == c:
            maxcnt = max(maxcnt, cnt)
            cnt = 0
        else:
            l = cnt
        maxcnt = max(maxcnt, l)
        mincnt = min(mincnt, maxcnt)
print(mincnt)
