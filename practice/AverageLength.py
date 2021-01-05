import itertools
n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
l = [x for x in range(n)]
all_route = list(itertools.permutations(l))
length = 0
cnt = 0
for route in all_route:
    xx, yy = point[route[0]][0], point[route[0]][1]
    num = 0
    for i in range(1, n):
        x, y = point[route[i]][0], point[route[i]][1]
        num += ((xx-x)**2+(yy-y)**2)**0.5
        xx, yy = x, y

    length += num
    cnt += 1
print(length/cnt)
