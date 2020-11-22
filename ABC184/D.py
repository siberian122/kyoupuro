l = list(map(int, input().split()))
ans = []
for i in l:
    if i == 0:
        ans.append(0)
        continue
    num = 100-i
    ans.append(num)
a = 0
for i in range(3):
    a += ans[i]*(l[i]/sum(l))
print(a)
print(ans)
