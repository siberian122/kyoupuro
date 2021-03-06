from collections import deque
n, m = map(int, input().split())
g = [[]for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


def bfs(u):
    queue = deque([u])
    d = [None]*n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v]+1
                queue.append(i)
    return d


d = bfs(0)
if d[n-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
