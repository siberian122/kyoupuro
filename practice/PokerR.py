k = int(input())
s = input()[:4]
t = input()[:4]

yama = [k] * 10
for i in s:
    yama[int(i)] -= 1
for i in t:
    yama[int(i)] -= 1


def point(te):
    hand = [0] * 10
    for i in te:
        hand[int(i)] += 1
    return sum(i*10**hand[i] for i in range(10))


ans = 0
for i in range(1, 10):
    if yama[i] == 0:
        continue
    # 2枚が違う数
    for j in range(1, 10):
        if i == j or yama[j] == 0:
            continue
        if point(s + str(i)) > point(t+str(j)):
            ans += yama[i]*yama[j]
    # 2枚が同じ数
    if yama[i] >= 2:
        if point(s+str(i)) > point(t + str(i)):
            ans += yama[i] * (yama[i]-1)
n = 9*k-8
print(ans/n/(n-1))
