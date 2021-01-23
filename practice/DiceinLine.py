n, k = map(int, input().split())
p = list(map(int, input().split()))
pp = [(1+x)/2 for x in p]
ruiseki = [0]
ans = 0
for i in range(n):
    ruiseki.append(ruiseki[i]+pp[i])
for i in range(n):
    if i+k <= n:
        ans = max(ans, ruiseki[i+k]-ruiseki[i])
print(ans)
