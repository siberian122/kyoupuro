n=int(input())
a=list(map(int,input().split()))
l=[0 for i in range(n)]
l[0]=a[0]
maxPoint=[0 for i in range(n)]
maxPoint[0]=a[0]
for i in range(1,n):
    l[i]=l[i-1]+a[i]
    if maxPoint[i-1]<l[i]:
        maxPoint[i]=l[i]
    else:
        maxPoint[i]=maxPoint[i-1]
#print(l,maxPoint)
cnt=0
ans=0
for i in range(n):
    num=cnt+maxPoint[i]
    cnt=cnt+l[i]
    ans=max(ans,num)
print(ans)