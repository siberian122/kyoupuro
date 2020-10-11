n,m=map(int,input().split())
w=list(map(int,input().split()))
w.sort()
l=[]
v=[]
for _ in range(m):
    a,b=map(int,input().split())
    l.append(a)
    v.append(b)
v=min(v)
cnt=0
g=0
for i in w:
    if v-g-i>0:
        g+=i
    else:
        cnt+=1
        g=0
ans=0
for i in range(cnt):
    ans+=l[i]
print(ans)