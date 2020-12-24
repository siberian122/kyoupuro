h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
yoko = [0]*h
tate = [0]*w
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            yoko[i] = 1
            tate[j] = 1

for i in range(h):
    if yoko[i]:
        for j in range(w):
            if tate[j]:
                print(a[i][j], end="")
        print()
