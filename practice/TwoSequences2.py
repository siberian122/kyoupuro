n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(n):
    c = max(c, max(a[:i+1])*b[i])
    print(c)
