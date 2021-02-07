
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
mae = -1
ushiro = -1
for i in range(h):
    ck = False
    for j in range(w):
        if s[i][j] == "#":
            if not ck and mae != j:
                # 前に何もなくて横もない
                ck = True
                ans += 1
                mae = j
            else:
                ck = True
        else:
            if ck and ushiro != j:
                ans += 1
                ck = False
                ushiro = j
            else:
                ck = False
    #print(mae, ushiro, ans)
    # print(ans)
mae = -1
ushiro = -1
for j in range(w):
    ck = False
    for i in range(h):
        if s[i][j] == "#":
            if not ck and mae != i:
                ans += 1
                ck = True
                mae = i
            else:
                ck = True
        else:
            if ck and ushiro != i:
                ans += 1
                ck = False
                ushiro = i
            else:
                ck = False

    # print(ans)
print(ans)

"""
.......
...#...
..###..
.#####.
.......
"""
