n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = 1
cnt = 0
for i in l:
    cnt += i
    if cnt <= x:
        ans += 1
    else:
        break
print(ans)
