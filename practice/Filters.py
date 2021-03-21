n = int(input())
low = -100
high = 100
add = 0
for _ in range(n):
    a, t = map(int, input().split())
    if t == 1:
        low += a
        high += a
        add += a
    elif t == 2:
        if low < a:
            low = a
        if high < a:
            high = a
    else:
        if low > a:
            low = a
        if high > a:
            high = a
q = int(input())
for x in list(map(int, input().split())):
    print(min(high, max(low, x + add)))
