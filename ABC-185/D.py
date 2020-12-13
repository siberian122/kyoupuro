n, m = map(int, input().split())
a = (list(map(int, input().split())))
a.insert(0, 0)
a.append(n+1)
a.sort()

num = 1e1000

ans = 0
for i in range(m+1):
    if a[i+1]-a[i]-1 != 0:
        num = min(num, a[i+1]-a[i]-1)

for i in range(m+1):
    leng = a[i+1]-a[i]-1

    ans += leng//num
    if leng % num != 0:
        ans += 1
print(int(ans))
