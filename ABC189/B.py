n, x = map(int, input().split())
for i in range(n):
    v, p = map(int, input().split())

    x -= float(v*p*0.01)
    print(x)
    if x < 0:
        exit(print(i+1))
print(-1)
