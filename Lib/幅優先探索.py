from collections import deque
n, m = map(int, input().split())
# n=頂点の数　m=辺の数
g = [[] for _ in range(n)]  # 隣接リスト

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


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


d = bfs(0)
print(d)  # 0からの距離
