n, l = map(int, input().split())
apple = sorted([x + l for x in range(n)])
cnt = 1000
for i in apple:
    if abs(i) < abs(cnt):
        cnt = i

print(sum(apple)-cnt)
