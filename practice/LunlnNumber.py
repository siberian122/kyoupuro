n = int(input())
lunlun = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0

while len(lunlun) < n:
    l = lunlun[i]
    x = l % 10
    if x == 0:
        lunlun.append(l*10)
        lunlun.append(l*10+1)
    elif x == 9:
        lunlun.append(l*10+8)
        lunlun.append(l*10+9)
    else:
        lunlun.append(l*10+x-1)
        lunlun.append(l*10+x)
        lunlun.append(l*10+x+1)
    i += 1
print(lunlun[n-1])
