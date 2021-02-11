n,m=map(int,input().split())
h=list(map(int,input().split()))

class UnionFind:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.sizes = [1] * (n + 1)

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        d1 = self.par[x]
        d2 = self.par[y]
        if d1 <= d2:
            self.par[y] = x
            self.sizes[x] = self.sizes[x] + self.sizes[y]
            if d1 == d2:
                self.par[x] = self.par[x] - 1
        else:
            self.par[x] = y
            self.sizes[y] = self.sizes[x] + self.sizes[y]

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    # サイズ
    def size(self, x):
        return self.sizes[self.find(x)]

    # 木の数
    def number(self):
        count = 0
        for i in self.par[1:]:
            if i < 0:
                count = count + 1
        return count

tree = UnionFind(n)
for _ in range(m):
    a,b=map(int,input().split())
    tree.union(a,b)

ans = 0
for i in range(n):
    now = h[i]
    for j in tree[i]:
        if now < h[j]:
            break
    ans +=1 
print(ans)

