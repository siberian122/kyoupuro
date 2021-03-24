n = int(input())
p = list(map(int, input().split()))
P = [x for x in range(1, n+1)]
cnt = 0
for i in range(n):
    if p[i] != P[i]:
        cnt += 1

if cnt < 3:
    print("YES")
else:
    print("NO")
