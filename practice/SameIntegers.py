l = list(map(int, input().split()))
s = sum(l)
m = max(l)
if (s-m) % 2 == 1:
    m += 1
print((m*3-s)//2)
