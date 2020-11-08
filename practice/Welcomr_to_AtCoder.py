n,m=map(int,input().split())
plo=[0 for _ in range(n+1)]
ans=[False for _ in range(n+1)]
A,W=0,0
for _ in range(m):
    p,s=input().split()
    if s=='WA':
        plo[int(p)]+=1
    else:
        if not ans[int(p)]:
            ans[int(p)]=True
            A+=1
            W+=plo[int(p)]
print(A, W)
        