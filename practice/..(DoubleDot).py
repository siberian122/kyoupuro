from collections import deque
n, m = map(int, input().split())

room = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    room[a].append(b)
    room[b].append(a)

l = [-1 for _ in range(n+1)]

d = deque()
d.append(1)
while d:
    p = d.popleft()
    for i in room[p]:
        if l[i] == -1:
            d.append(i)
            l[i] = p
print(d)
print(l)
print("Yes")

a = l[2:]
for i in range(len(a)):
    print(a[i])
