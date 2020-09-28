n,k=map(int,input().split())
a=list(map(int,input().split()))
now=0
l=[1]
ll=[]
for i in range(n*2):
    now=a[now]
    if now not in l:
        l.append(now)
    elif now in l and now not in ll:
        ll.append(now)
    else:
        break
    now-=1
b=len(l)
c=len(ll)
num=b-c
if k>num:
    k=(k-num)%c
    print(ll[k])
else:
    k=k%b
    print(l[k])