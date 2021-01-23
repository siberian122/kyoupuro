n, k = map(int, input().split())
p = list(map(int, input().split()))
pp = [(1+x)/2 for x in p]
ruiseki = [pp[0]]
ans = 0
for i in range(1, n):
    ruiseki.append(ruiseki[i-1]+pp[i])
print(len(ruiseki))
for i in range(n-k):
    ans = max(ans, ruiseki[i+k]-ruiseki[i])
print(ans)
