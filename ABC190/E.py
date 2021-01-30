from collections import deque
n, m = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
k = int(input())
c = list(map(int, input().split()))


def bfs(u):
    queue = deque([u])
    d = [None]*n  # uからの距離の初期化
    d[u] = 0  # 自身との距離
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v]+1
                queue.append(i)
    return d


ans = []
d = bfs(c[0]-1)
for i in c:
    if d[i-1] == None:
        exit(print(-1))
    ans.append(d[i-1])
print(sum(ans)+1)
