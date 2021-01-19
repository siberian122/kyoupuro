l, r = map(int, input().split())
num = r-l
ans = 2020
if num >= 2019:
    ans = 0
else:
    for i in range(l, r):
        for j in range(l+1, r+1):
            ans = min(ans, (i*j) % 2019)
print(ans)
