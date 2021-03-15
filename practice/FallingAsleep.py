n = int(input())
ans = 0
music = []
for _ in range(n):
    s, t = (input().split())
    t = int(t)
    music.append([s, t])
X = input()
chk = False
for i in range(n):
    if chk:
        ans += music[i][1]
    else:
        if X == music[i][0]:
            chk = True
print(ans)
