n = int(input())
t = 0
cnt_x = 0
cnt_y = 0
for _ in range(n):
    tt, x, y = map(int, input().split())
    if (abs(cnt_x-x)+abs(cnt_y-y)) > abs(tt-t) or (x+y+tt) % 2 != 0:
        exit(print("No"))
    t, cnt_x, cnt_y = tt, x, y
print("Yes")
