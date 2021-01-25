n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
ma = 0
for i in range(n):
    ma = max(ma, a[i])
    c = max(c, ma*b[i])
    print(c)
