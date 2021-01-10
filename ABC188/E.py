import heapq
import collections
n, m = map(int, input().split())
a = list(map(int, input().split()))


class Dijkstra():
    def __init__(self, N):
        self.N = N
        self.e = [[float('inf') for i in range(self.N)] for i in range(N)]

    def add(self, u, v, d, directed=False):
        """
        0-indexedでなくてもよいことに注意
        u = from, v = to, d = cost
        directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u][v] = d
            self.e[v][u] = d
        else:
            self.e[u][v] = d

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        0-indexedであることに注意
        s =  始点
        return: 始点から各点までの最短経路
        """
        d = [float('inf') for i in range(self.N)]
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue

            for uv, ud in enumerate(self.e[u]):
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    def getDijkstraPath(self, s, t):
        # sからtへの最短経路の経路復元
        prev = [s] * self.N  # 最短経路の直前の頂点
        d = [float("inf")] * self.N
        used = [False] * self.N
        d[s] = 0

        while True:
            v = -1
            for i in range(self.N):
                if (not used[i]) and (v == -1):
                    v = i
                elif (not used[i]) and d[i] < d[v]:
                    v = i
            if v == -1:
                break
            used[v] = True

            for i in range(self.N):
                if d[i] > d[v] + self.e[v][i]:
                    d[i] = d[v] + self.e[v][i]
                    prev[i] = v

        path = [t]
        while prev[t] != s:
            path.append(prev[t])
            prev[t] = prev[prev[t]]
        path.append(s)
        path = path[::-1]
        return path


for _ in range(n):
