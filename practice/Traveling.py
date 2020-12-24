n = int(input())
ans = "No"
t = 0
cnt_x = 0
cnt_y = 0
for _ in range(n):
    tt, x, y = map(int, input().split())
    time = tt-t
    num = abs(cnt_x-x)+abs(cnt_y-y)
    if num <= t and t % 2 == num % 2:
        ans = "Yes"
    else:
        ans = 'No'
    t, cnt_x, cnt_y = tt, x, y
print(ans)
