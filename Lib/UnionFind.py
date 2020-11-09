def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x]==rank[y]:rank[x]+=1
