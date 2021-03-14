n = int(input())
ans = 0
cnt = 1
while cnt < n:
    ans += n/(n-cnt)
    cnt += 1
print(ans)
