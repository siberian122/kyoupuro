k, a, b = map(int, input().split())
bis, yen = 1, 0
for i in range(k):
    if yen > 0:
        bis += yen*b
        yen = 0
    elif a <= bis and k-i > 1:
        bis -= a
        yen += 1
    else:
        bis += 1
    #print(bis, yen)
print(bis)
