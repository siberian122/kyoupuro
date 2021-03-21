n = int(input())
a = []
t = []
mae = 0
cnt = 0
chk = False
for _ in range(n):
    A, T = map(int, input().split())
    if mae == T:
        if T == 1:
            a[-1] += A
        elif T == 2:
            a[-1] = max(A, a[-1])
        else:
            a[-1] = min(A, a[-1])
    else:
        a.append(A)
        t.append(T)
        mae = T
        cnt += 1
q = int(input())
x = list(map(int, input().split()))

for i in x:
    for j in range(cnt):
        if t[j] == 1:
            i += a[j]
        elif t[j] == 2:
            i = max(i, a[j])
        else:
            i = min(i, a[j])
    print(i)
