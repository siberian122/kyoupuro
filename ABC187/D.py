n = int(input())
l = []
aoki = 0
taka = 0
for i in range(n):
    a, t = map(int, input().split())
    aoki += a

    cnt = [a, t, a+t]
    l.append(cnt)
l = sorted(l, reverse=True, key=lambda x:  x[2])
ans = 0
aokii = aoki
for i in range(n):
    taka += l[i][0]+l[i][1]
    aoki -= l[i][0]
    if aoki < taka:
        ans = i+1
        break
l = sorted(l, reverse=True, key=lambda x: x[0])
taka = 0
for i in range(n):
    taka += l[i][-1]
    aokii -= l[i][0]
    if aokii < taka:
        ans = i+1
print(ans)
#print(aoki, taka)
# print(l)
