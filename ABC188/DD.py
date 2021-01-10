n, C = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data = sorted(data, key=lambda x: x[0])
a, b, c = data[0][0], data[0][1], data[0][2]
ans = 0
cnt = 0
for i in range(n-1):
    cnt = 0
    for l in range(1, n):
        aa, bb, cc = data[l][0], data[l][1], data[l][2]
        if a <= aa <= b:
            num = min(b, bb)-aa-1
            cnt += num*cc
            if num*c+num*cc > C:
