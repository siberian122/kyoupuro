n, x = map(int, input().split())
l = list(map(int, input().split()))
ll = [l[i-1]+l[i] for i in range(1, n)]
for i in range(n):
    if ll[i] > x:
        print(i)
        break
