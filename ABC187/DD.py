n = int(input())
l = []
aoki = 0
taka = 0
for i in range(n):
    a, t = map(int, input().split())
    aoki += a

    cnt = [a, t, a-t]
    l.append(cnt)
l = sorted(l, reverse=True, key=lambda x:  x[2])
for i in range(n):
    taka += l[i][0]+l[i][1]
    aoki -= l[i][0]
    if aoki < taka:
        print(i+1)
        break
#print(aoki, taka)
# print(l)
