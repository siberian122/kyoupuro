h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
x -= 1
y -= 1
for i in range(x, h):
    if s[i][y] == ".":
        ans += 1
    else:
        break
for i in reversed(range(0, x)):
    if s[i][y] == ".":
        ans += 1
    else:
        break
for i in range(y, w):
    if s[x][i] == ".":
        ans += 1
    else:
        break
for i in reversed(range(0, y)):
    if s[x][i] == ".":
        ans += 1
    else:
        break
print(ans - 1)
