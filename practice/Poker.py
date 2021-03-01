from collections import Counter
k = int(input())
s = input()[:-1]
t = input()[:-1]
s_point, t_point = 0, 0
tt = [0] * 10
ss = [0] * 10
for i in s:
    ss[int(i)] += 1
for i in t:
    tt[int(i)] += 1
s_point = sum(x*10**ss[x] for x in range(10))
t_point = sum(x*10**tt[x] for x in range(10))
# print(s_point, t_point)
total = [k-ss[i]+tt[i] for i in range(10)]
# どうやって確立を求める？？
# 全探索？？
