x, y = map(int, input().split())
ans = 0
for i in range(1000):
    if 2**i*x > y:
        break
    ans = i
print(ans+1)
