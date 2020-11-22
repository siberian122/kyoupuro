n, t = map(int, input().split())
a = list(map(int, input().split()))
b = a[:20]
c = a[20:]
b_sum = [0]
c_sum = [0]
for i in b:
    for j in range(len(b_sum)):
        b_sum.append(b_sum[j]+i)  # 前20個までのそれぞれ組み合わせの分数
for i in c:
    for j in range(len(c_sum)):
        c_sum.append(c_sum[j]+i)  # 前と同様
b_sum.sort()
c_sum.sort()
#print(b_sum, c_sum)
i = len(c_sum)-1
ans = 0
for x in b_sum:
    # 前と後ろの組み合わせで最大のものをとる
    while i >= 0 and c_sum[i]+x > t:
        i -= 1
    if i < 0:
        break
    ans = max(ans, x+c_sum[i])
print(ans)
