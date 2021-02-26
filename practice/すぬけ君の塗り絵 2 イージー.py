w, h, n = map(int, input().split())
yoko = 0
tate = 0
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        yoko = max(yoko, x)
    elif a == 2:
        w = min(w, x)
    elif a == 3:
        tate = max(tate, y)
    elif a == 4:
        h = min(h, y)
# print(h, tate, w, yoko)
print(max(w-yoko, 0)*max(h-tate, 0))
