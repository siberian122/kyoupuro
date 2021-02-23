w, h, x, y = map(int, input().split())
if 2*x == w and 2*y == h:
    ans = 1
else:
    ans = 0
print(w*h/2, ans)
