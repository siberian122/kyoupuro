n, m = map(int, input().split())

jyouken = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
l = [list(map(int, input().split())) for _ in range(k)]
ans = []
for i in range(2**k):
    ll = []
    cnt = 0
    for j in range(k):
        if ((i >> j) & 1):
            ll.append(l[j][0])
        else:
            ll.append(l[j][1])

    for u in jyouken:
        if u[0] in ll and u[1] in ll:
            cnt += 1
    ans.append(cnt)
print(max(ans))
