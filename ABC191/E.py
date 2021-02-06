from heapq import heappush, heappop
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((1, b))
    edges[b].append((1, a))

INF = 10 ** 9
dist = [INF] * n
prev = [-1] * n


def dijkstra(s):
    q = [(0, s)]
    dist[s] = 0
    while q:
        v = heappop(q)[1]
        for cost, to in edges[v]:
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                prev[to] = v
                heappush(q, (dist[to], to))


for i in range(n):
    dijkstra(i)
